type FontSize = "s" | "m" | "l" | "xl";
type Width = "narrow" | "medium" | "wide";
type ThemePref = "light" | "dark" | "system";

interface ReaderState {
  theme: ThemePref;
  fontSize: FontSize;
  width: Width;
  current: number | null;
  opened: number[];
  scroll: Record<string, number>;
}

interface CatalogItem {
  n: number;
  t: string;
  h: string;
  w?: number;
}

const STORAGE_KEY = "murim-reader";
const LEGACY_THEME = "murim-theme";
const LEGACY_CHAPTER = "murim-chapter";
const SIZES: FontSize[] = ["s", "m", "l", "xl"];
const WIDTHS: Width[] = ["narrow", "medium", "wide"];
const JUMP_LIMIT = 10;
const JUMP_NEAR = 9;
const READ_THRESHOLD = 0.95;

const root = document.documentElement;
const base = root.getAttribute("data-base") || "/";

let state = loadState();
let catalog: CatalogItem[] | null = null;
let catalogPromise: Promise<CatalogItem[]> | null = null;
let jumpItems: CatalogItem[] = [];
let jumpIndex = -1;
let chromeReady = false;
let pageAbort: AbortController | null = null;
let wordWeights: Map<number, number> | null = null;

document.addEventListener("astro:page-load", boot);
boot();

function boot() {
  state = loadState();
  applyPrefs(state);
  if (!chromeReady) {
    initSettings();
    initJump();
    initKeys();
    chromeReady = true;
  }
  pageAbort?.abort();
  pageAbort = new AbortController();
  const { signal } = pageAbort;
  syncProgressChrome();
  initIndex(signal);
  initChapter(signal);
}

function defaultState(): ReaderState {
  return {
    theme: "system",
    fontSize: "m",
    width: "medium",
    current: null,
    opened: [],
    scroll: {},
  };
}

function loadState(): ReaderState {
  const fallback = defaultState();
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      return normalize(JSON.parse(raw) as Partial<ReaderState>, fallback);
    }
  } catch {
    /* use fallback / legacy */
  }
  const legacyTheme = localStorage.getItem(LEGACY_THEME);
  const legacyChapter = localStorage.getItem(LEGACY_CHAPTER);
  if (legacyTheme === "light" || legacyTheme === "dark" || legacyTheme === "system") {
    fallback.theme = legacyTheme;
  }
  const chapter = Number.parseInt(legacyChapter ?? "", 10);
  if (Number.isInteger(chapter)) {
    fallback.current = chapter;
    fallback.opened = [chapter];
  }
  return fallback;
}

function normalize(raw: Partial<ReaderState>, fallback: ReaderState): ReaderState {
  const theme = raw.theme === "light" || raw.theme === "dark" || raw.theme === "system" ? raw.theme : fallback.theme;
  const fontSize = SIZES.includes(raw.fontSize as FontSize) ? (raw.fontSize as FontSize) : fallback.fontSize;
  const width = WIDTHS.includes(raw.width as Width) ? (raw.width as Width) : fallback.width;
  const current = typeof raw.current === "number" && Number.isInteger(raw.current) ? raw.current : null;
  const opened = Array.isArray(raw.opened)
    ? [...new Set(raw.opened.filter((value) => Number.isInteger(value)))]
    : [];
  const scroll: Record<string, number> = {};
  if (raw.scroll && typeof raw.scroll === "object") {
    for (const [key, value] of Object.entries(raw.scroll)) {
      if (typeof value === "number" && Number.isFinite(value)) {
        scroll[key] = clamp(value, 0, 1);
      }
    }
  }
  return { theme, fontSize, width, current, opened, scroll };
}

function saveState() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch {
    /* private mode / quota */
  }
}

function applyPrefs(next: ReaderState) {
  const dark =
    next.theme === "dark" || (next.theme !== "light" && window.matchMedia("(prefers-color-scheme: dark)").matches);
  root.dataset.theme = dark ? "dark" : "light";
  root.dataset.pfTheme = dark ? "dark" : "light";
  root.dataset.size = next.fontSize;
  root.dataset.width = next.width;
}

function clamp(value: number, min: number, max: number) {
  return Math.min(max, Math.max(min, value));
}

function withBase(path: string) {
  return `${base.replace(/\/?$/, "/")}${path.replace(/^\//, "")}`;
}

function chapterUrl(chapter: number) {
  return withBase(`chapter/${chapter}/`);
}

function loadCatalog() {
  if (catalog) {
    return Promise.resolve(catalog);
  }
  catalogPromise ??= fetch(withBase("chapters.json"))
    .then((response) => {
      if (!response.ok) {
        throw new Error("catalog");
      }
      return response.json() as Promise<CatalogItem[]>;
    })
    .then((items) => {
      catalog = items;
      ingestWordWeights(items);
      return items;
    })
    .catch(() => {
      catalogPromise = null;
      return [] as CatalogItem[];
    });
  return catalogPromise;
}

function ingestWordWeights(items: CatalogItem[]) {
  if (!items.some((item) => typeof item.w === "number")) {
    return;
  }
  const map = new Map<number, number>();
  for (const item of items) {
    map.set(item.n, typeof item.w === "number" && item.w > 0 ? item.w : 1);
  }
  wordWeights = map;
}

function ensureWordWeightsFromPage() {
  if (wordWeights) {
    return;
  }
  const page = document.querySelector<HTMLElement>("[data-page='index']");
  const raw = page?.dataset.words;
  if (!raw) {
    return;
  }
  try {
    const parsed = JSON.parse(raw) as Record<string, number>;
    const map = new Map<number, number>();
    for (const [key, value] of Object.entries(parsed)) {
      const chapter = Number.parseInt(key, 10);
      if (Number.isInteger(chapter) && typeof value === "number" && value > 0) {
        map.set(chapter, value);
      }
    }
    if (map.size) {
      wordWeights = map;
    }
  } catch {
    /* ignore bad embed */
  }
}

function syncProgressChrome() {
  const onChapter = Boolean(document.querySelector("[data-page='chapter']"));
  const progress = document.getElementById("read-progress");
  const label = document.getElementById("read-progress-label");
  if (progress) {
    progress.hidden = !onChapter;
  }
  if (label) {
    label.hidden = !onChapter;
    if (!onChapter) {
      label.textContent = "0%";
    }
  }
  document.getElementById("site-header")?.classList.remove("is-hidden");
  document.getElementById("chapter-dock")?.classList.remove("is-hidden");
}

function lockBodyScroll() {
  if (document.documentElement.dataset.scrollLocked === "1") {
    return;
  }
  const y = window.scrollY;
  document.documentElement.dataset.scrollLocked = "1";
  document.documentElement.style.overflow = "hidden";
  document.body.style.position = "fixed";
  document.body.style.top = `-${y}px`;
  document.body.style.left = "0";
  document.body.style.right = "0";
  document.body.style.width = "100%";
  document.body.dataset.scrollY = String(y);
}

function unlockBodyScroll() {
  if (document.documentElement.dataset.scrollLocked !== "1") {
    return;
  }
  if (document.querySelector("dialog[open]")) {
    return;
  }
  const y = Number.parseInt(document.body.dataset.scrollY ?? "0", 10) || 0;
  delete document.documentElement.dataset.scrollLocked;
  document.documentElement.style.overflow = "";
  document.body.style.position = "";
  document.body.style.top = "";
  document.body.style.left = "";
  document.body.style.right = "";
  document.body.style.width = "";
  delete document.body.dataset.scrollY;
  window.scrollTo(0, y);
}

function bindDialogScrollLock(dialog: HTMLDialogElement) {
  dialog.addEventListener("close", () => unlockBodyScroll());
  dialog.addEventListener("cancel", () => {
    // unlock runs on close; keep for Safari cancel path
    queueMicrotask(() => unlockBodyScroll());
  });
}

function openDialog(dialog: HTMLDialogElement) {
  lockBodyScroll();
  dialog.showModal();
}

function initSettings() {
  const dialog = document.getElementById("settings-dialog") as HTMLDialogElement | null;
  const openBtn = document.getElementById("settings-open");
  const closeBtn = document.getElementById("settings-close");
  if (!dialog || !openBtn) {
    return;
  }

  const syncInputs = () => {
    const resolved = root.dataset.theme === "dark" ? "dark" : "light";
    checkRadio(dialog, "theme", resolved);
    checkRadio(dialog, "size", state.fontSize);
    checkRadio(dialog, "width", state.width);
  };

  bindDialogScrollLock(dialog);
  openBtn.addEventListener("click", () => {
    syncInputs();
    openDialog(dialog);
  });
  closeBtn?.addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) {
      dialog.close();
    }
  });
  dialog.addEventListener("change", (event) => {
    const input = event.target as HTMLInputElement;
    if (input.name === "theme" && (input.value === "light" || input.value === "dark")) {
      state.theme = input.value;
    }
    if (input.name === "size" && SIZES.includes(input.value as FontSize)) {
      state.fontSize = input.value as FontSize;
    }
    if (input.name === "width" && WIDTHS.includes(input.value as Width)) {
      state.width = input.value as Width;
    }
    applyPrefs(state);
    saveState();
  });
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => {
    if (state.theme === "system") {
      applyPrefs(state);
    }
  });
}

function checkRadio(rootEl: Element, name: string, value: string) {
  const input = rootEl.querySelector<HTMLInputElement>(`input[name="${name}"][value="${value}"]`);
  if (input) {
    input.checked = true;
  }
}

function initJump() {
  const dialog = document.getElementById("jump-dialog") as HTMLDialogElement | null;
  const openBtn = document.getElementById("jump-open");
  const closeBtn = document.getElementById("jump-close");
  const input = document.getElementById("jump-input") as HTMLInputElement | null;
  const results = document.getElementById("jump-results");
  if (!dialog || !openBtn || !input || !results) {
    return;
  }

  const open = () => {
    input.value = "";
    openDialog(dialog);
    input.focus();
    void renderJump("", results);
  };

  bindDialogScrollLock(dialog);
  openBtn.addEventListener("click", open);
  closeBtn?.addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) {
      dialog.close();
    }
  });
  input.addEventListener("input", () => {
    void renderJump(input.value, results);
  });
  input.addEventListener("keydown", (event) => {
    if (event.key === "ArrowDown") {
      event.preventDefault();
      moveJump(1, results);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      moveJump(-1, results);
    } else if (event.key === "Enter") {
      event.preventDefault();
      const target = jumpItems[jumpIndex] ?? jumpItems[0];
      if (target) {
        location.href = target.h;
      }
    }
  });
}

async function renderJump(query: string, list: HTMLElement) {
  const items = digitsOf(query)
    ? matchChapters(await loadCatalog(), query)
    : nearbyChapters(await loadCatalog(), state.current);
  jumpItems = items;
  if (digitsOf(query)) {
    jumpIndex = items.length ? 0 : -1;
  } else {
    const currentAt = items.findIndex((item) => item.n === state.current);
    jumpIndex = currentAt >= 0 ? currentAt : items.length ? 0 : -1;
  }
  list.replaceChildren();
  if (!items.length) {
    if (!digitsOf(query)) {
      list.hidden = true;
      return;
    }
    list.hidden = false;
    const empty = document.createElement("li");
    empty.className = "jump-empty";
    empty.textContent = "No matching chapter";
    list.append(empty);
    return;
  }
  list.hidden = false;
  for (const item of items) {
    const li = document.createElement("li");
    const button = document.createElement("a");
    button.href = item.h;
    button.id = `jump-opt-${item.n}`;
    button.className = "jump-option";
    button.setAttribute("role", "option");
    button.textContent = item.t;
    if (item.n === state.current) {
      button.classList.add("is-current");
    }
    li.append(button);
    list.append(li);
  }
  paintJump(list);
}

function moveJump(delta: number, list: HTMLElement) {
  if (!jumpItems.length) {
    return;
  }
  jumpIndex = (jumpIndex + delta + jumpItems.length) % jumpItems.length;
  paintJump(list);
}

function paintJump(list: HTMLElement) {
  const options = list.querySelectorAll<HTMLElement>(".jump-option");
  options.forEach((option, index) => {
    const selected = index === jumpIndex;
    option.setAttribute("aria-selected", selected ? "true" : "false");
    option.classList.toggle("is-active", selected);
    if (selected) {
      option.scrollIntoView({ block: "nearest" });
    }
  });
}

function digitsOf(query: string) {
  return query.replace(/\D/g, "");
}

function nearbyChapters(items: CatalogItem[], current: number | null): CatalogItem[] {
  if (!items.length) {
    return [];
  }
  const found = current != null ? items.findIndex((item) => item.n === current) : 0;
  const center = found >= 0 ? found : 0;
  const before = Math.floor((JUMP_NEAR - 1) / 2);
  let start = Math.max(0, center - before);
  let end = Math.min(items.length, start + JUMP_NEAR);
  start = Math.max(0, end - JUMP_NEAR);
  return items.slice(start, end);
}

function matchChapters(items: CatalogItem[], query: string): CatalogItem[] {
  const q = digitsOf(query);
  if (!q) {
    return [];
  }
  const exact = items.filter((item) => String(item.n) === q);
  const rest = items
    .filter((item) => String(item.n).startsWith(q) && String(item.n) !== q)
    .sort((left, right) => left.n - right.n);
  return [...exact, ...rest].slice(0, JUMP_LIMIT);
}

function initIndex(signal: AbortSignal) {
  const page = document.querySelector<HTMLElement>("[data-page='index']");
  if (!page) {
    return;
  }
  ensureWordWeightsFromPage();
  const total = Number(page.dataset.count || 0);
  const continueBtn = document.getElementById("continue") as HTMLAnchorElement | null;
  const startBtn = document.getElementById("start");
  const progress = document.getElementById("overall-progress");
  const label = document.getElementById("overall-label");
  const fill = document.getElementById("overall-fill");
  const bar = document.getElementById("overall-bar");
  const filter = document.getElementById("chapter-filter") as HTMLInputElement | null;

  if (state.current != null && continueBtn) {
    continueBtn.href = chapterUrl(state.current);
    continueBtn.hidden = false;
    startBtn?.setAttribute("hidden", "");
  }

  if (state.current != null && progress && label && fill) {
    const fraction = overallFraction(total);
    const percent = Math.round(fraction * 100);
    progress.hidden = false;
    label.textContent = `Chapter ${state.current} of ${total} · ${percent}% by words`;
    fill.style.transform = `scaleX(${fraction})`;
    if (bar) {
      bar.setAttribute("aria-valuenow", String(percent));
      bar.setAttribute("aria-label", `${percent}% of the book by words`);
    }
  }

  paintIndexList("");
  filter?.addEventListener("input", () => paintIndexList(filter.value), { signal });
  void loadCatalog();
}

function overallFraction(total: number) {
  ensureWordWeightsFromPage();
  if (wordWeights && wordWeights.size) {
    let read = 0;
    let words = 0;
    for (const [chapter, weight] of wordWeights) {
      words += weight;
      read += clamp(state.scroll[String(chapter)] ?? 0, 0, 1) * weight;
    }
    return words ? clamp(read / words, 0, 1) : 0;
  }
  if (!total) {
    return 0;
  }
  let read = 0;
  for (const value of Object.values(state.scroll)) {
    read += clamp(value, 0, 1);
  }
  return clamp(read / total, 0, 1);
}

function paintIndexList(query: string) {
  const q = query.trim().toLowerCase();
  const filtering = q.length > 0;
  document.querySelectorAll<HTMLDetailsElement>("details.chapter-range").forEach((range) => {
    let visible = 0;
    range.querySelectorAll<HTMLAnchorElement>("a[data-chapter]").forEach((link) => {
      const chapter = Number(link.dataset.chapter);
      const haystack = `${chapter} ${link.textContent ?? ""}`.toLowerCase();
      const show = !filtering || haystack.includes(q);
      const item = link.closest("li");
      if (item) {
        item.hidden = !show;
      }
      if (show) {
        visible += 1;
      }
      const isCurrent = chapter === state.current;
      const isRead = (state.scroll[String(chapter)] ?? 0) >= READ_THRESHOLD;
      link.classList.toggle("is-current", isCurrent);
      link.classList.toggle("is-read", isRead && !isCurrent);
      if (isCurrent) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });
    range.hidden = filtering && visible === 0;
    const start = Number(range.dataset.start);
    const end = Number(range.dataset.end);
    const containsCurrent = state.current != null && state.current >= start && state.current <= end;
    range.open = filtering ? visible > 0 : containsCurrent;
  });
}

function initChapter(signal: AbortSignal) {
  const page = document.querySelector<HTMLElement>("[data-page='chapter']");
  if (!page) {
    return;
  }
  const chapter = Number(page.dataset.chapter);
  if (!Number.isInteger(chapter)) {
    return;
  }

  state.current = chapter;
  if (!state.opened.includes(chapter)) {
    state.opened.push(chapter);
  }
  saveState();

  const bar = document.getElementById("read-progress-bar");
  const progress = document.getElementById("read-progress");
  const label = document.getElementById("read-progress-label");
  const header = document.getElementById("site-header");
  const dock = document.getElementById("chapter-dock");
  const topBtn = document.getElementById("dock-top");
  const bottomBtn = document.getElementById("dock-bottom");

  const maxScroll = () => Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
  const fraction = () => {
    const max = maxScroll();
    return max === 0 ? 1 : clamp(window.scrollY / max, 0, 1);
  };
  const paint = () => {
    const value = fraction();
    const percent = Math.round(value * 100);
    if (bar) {
      bar.style.transform = `scaleX(${value})`;
    }
    if (label) {
      label.hidden = false;
      label.textContent = `${percent}%`;
    }
    if (progress) {
      progress.hidden = false;
      progress.setAttribute("aria-valuenow", String(percent));
      progress.setAttribute("aria-valuetext", `${percent}% of chapter`);
    }
  };
  const persist = () => {
    state.scroll[String(chapter)] = fraction();
    saveState();
  };
  let persistTimer = 0;
  const persistSoon = () => {
    if (persistTimer) {
      return;
    }
    persistTimer = window.setTimeout(() => {
      persistTimer = 0;
      persist();
    }, 180);
  };

  if (!location.hash) {
    history.scrollRestoration = "manual";
    const saved = state.scroll[String(chapter)];
    if (saved && saved > 0) {
      window.scrollTo(0, saved * maxScroll());
    }
  }
  persist();
  paint();
  header?.classList.remove("is-hidden");
  dock?.classList.remove("is-hidden");

  topBtn?.addEventListener(
    "click",
    () => {
      const behavior = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth";
      window.scrollTo({ top: 0, behavior });
    },
    { signal },
  );
  bottomBtn?.addEventListener(
    "click",
    () => {
      const behavior = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth";
      window.scrollTo({ top: maxScroll(), behavior });
    },
    { signal },
  );

  let lastY = window.scrollY;
  let ticking = false;
  window.addEventListener(
    "scroll",
    () => {
      if (ticking) {
        return;
      }
      ticking = true;
      requestAnimationFrame(() => {
        const y = window.scrollY;
        paint();
        persistSoon();
        const hide = y > lastY && y > 72;
        header?.classList.toggle("is-hidden", hide);
        dock?.classList.toggle("is-hidden", hide);
        lastY = y;
        ticking = false;
      });
    },
    { passive: true, signal },
  );
  window.addEventListener(
    "resize",
    () => {
      paint();
      persistSoon();
    },
    { signal },
  );
  window.addEventListener("pagehide", persist, { signal });
  signal.addEventListener("abort", () => {
    if (persistTimer) {
      window.clearTimeout(persistTimer);
      persistTimer = 0;
    }
    persist();
  });
}

function initKeys() {
  document.addEventListener("keydown", (event) => {
    if (event.target instanceof Element && event.target.closest("input, textarea, select, dialog")) {
      return;
    }
    if (document.querySelector("dialog[open]")) {
      return;
    }
    const key = event.key === "ArrowLeft" ? "prev" : event.key === "ArrowRight" ? "next" : "";
    if (key) {
      document.querySelector<HTMLAnchorElement>(`[data-nav="${key}"]`)?.click();
    }
  });
}
