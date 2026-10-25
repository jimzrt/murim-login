import fs from "node:fs";
import path from "node:path";

import { SOURCE_CHAPTER_MAX, SOURCE_CHAPTER_TOTAL } from "../generated/source-count";

const CHAPTER = /^\d{4}$/;

export interface TranslationProgress {
  sourceTotal: number;
  sourceMax: number;
  translated: number[];
  translatedCount: number;
  /** Source chapters (0..sourceMax) without a translation yet. */
  missing: number[];
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

export function loadTranslationProgress(): TranslationProgress {
  const translated = chapterNumbers(path.join(repoRoot(), "translations"), ".md");
  const have = new Set(translated);
  const missing: number[] = [];
  for (let chapter = 0; chapter <= SOURCE_CHAPTER_MAX; chapter++) {
    if (!have.has(chapter)) {
      missing.push(chapter);
    }
  }
  return {
    sourceTotal: SOURCE_CHAPTER_TOTAL,
    sourceMax: SOURCE_CHAPTER_MAX,
    translated,
    translatedCount: translated.filter((chapter) => chapter <= SOURCE_CHAPTER_MAX).length,
    missing,
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
