import fs from "node:fs";
import path from "node:path";

const CHAPTER = /^\d{4}$/;

export interface TranslationProgress {
  sourceTotal: number;
  translated: number[];
  mastered: number[];
  translatedCount: number;
  masteredCount: number;
  sourceMax: number;
}

/**
 * Repo root is the parent of `reader/`. Astro inlines it from `astro.config.ts`
 * (`import.meta.env.MURIM_ROOT`). Build scripts may set `process.env.MURIM_ROOT`.
 */
export function repoRoot(): string {
  const fromAstro =
    typeof import.meta.env === "object" && import.meta.env && import.meta.env.MURIM_ROOT;
  const configured = (typeof fromAstro === "string" && fromAstro) || process.env.MURIM_ROOT;
  if (!configured) {
    throw new Error("MURIM_ROOT is not set");
  }
  return path.resolve(configured);
}

function chapterNumbers(dir: string, ext: string): number[] {
  if (!fs.existsSync(dir)) {
    return [];
  }
  return fs
    .readdirSync(dir)
    .filter((name) => name.endsWith(ext) && CHAPTER.test(path.parse(name).name))
    .map((name) => Number.parseInt(path.parse(name).name, 10))
    .filter((n) => Number.isInteger(n))
    .sort((a, b) => a - b);
}

function isPromoted(root: string, chapter: number): boolean {
  const statePath = path.join(
    root,
    "reviews",
    "mastering",
    String(chapter).padStart(4, "0"),
    "state.json",
  );
  if (!fs.existsSync(statePath)) {
    return false;
  }
  try {
    const state = JSON.parse(fs.readFileSync(statePath, "utf8")) as {
      stage?: string;
      qa_passed?: boolean;
    };
    return state.stage === "PROMOTED" && Boolean(state.qa_passed);
  } catch {
    return false;
  }
}

export function loadTranslationProgress(): TranslationProgress {
  const root = repoRoot();
  const source = chapterNumbers(path.join(root, "source"), ".txt");
  const translated = chapterNumbers(path.join(root, "translations"), ".md");
  const mastered = translated.filter((chapter) => isPromoted(root, chapter));
  return {
    sourceTotal: source.length,
    translated,
    mastered,
    translatedCount: translated.length,
    masteredCount: mastered.length,
    sourceMax: source.length ? source[source.length - 1]! : 0,
  };
}

export function percent(part: number, whole: number): number {
  if (whole <= 0) {
    return 0;
  }
  return Math.min(100, Math.round((part / whole) * 1000) / 10);
}

/** Collapse sorted chapter numbers into "0–66, 70, 72–74". */
export function formatRanges(numbers: number[]): string {
  if (!numbers.length) {
    return "none";
  }
  const parts: string[] = [];
  let start = numbers[0]!;
  let prev = numbers[0]!;
  for (let i = 1; i <= numbers.length; i++) {
    const current = numbers[i];
    if (current === prev + 1) {
      prev = current;
      continue;
    }
    parts.push(start === prev ? String(start) : `${start}–${prev}`);
    if (current != null) {
      start = current;
      prev = current;
    }
  }
  return parts.join(", ");
}
