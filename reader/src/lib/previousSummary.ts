import { readFile } from "node:fs/promises";
import path from "node:path";
import { markdownToHtml } from "satteri";

import { repoRoot } from "./progress";

const SUMMARY_INTERVAL = 5;

export interface PreviousSummary {
  start: number;
  end: number;
  label: string;
  html: string;
}

export function previousBlockRange(chapter: number): { start: number; end: number } | null {
  if (chapter < SUMMARY_INTERVAL) {
    return null;
  }
  const currentStart = Math.floor(chapter / SUMMARY_INTERVAL) * SUMMARY_INTERVAL;
  const start = currentStart - SUMMARY_INTERVAL;
  return { start, end: start + SUMMARY_INTERVAL - 1 };
}

function extractPlot(markdown: string): string | null {
  const heading = markdown.match(/^##\s+Plot\s*\r?\n/m);
  if (!heading || heading.index == null) {
    return null;
  }
  const from = heading.index + heading[0].length;
  const rest = markdown.slice(from);
  const next = rest.search(/^##\s+/m);
  const plot = (next === -1 ? rest : rest.slice(0, next)).trim();
  return plot || null;
}

function pad(n: number): string {
  return String(n).padStart(4, "0");
}

export async function loadPreviousSummary(chapter: number): Promise<PreviousSummary | null> {
  const range = previousBlockRange(chapter);
  if (!range) {
    return null;
  }

  const summaryPath = path.join(
    repoRoot(),
    "summaries",
    `${pad(range.start)}-${pad(range.end)}.md`,
  );
  let raw: string;
  try {
    raw = await readFile(summaryPath, "utf8");
  } catch {
    return null;
  }

  const plot = extractPlot(raw);
  if (!plot) {
    return null;
  }

  const { html } = await markdownToHtml(plot);
  return {
    start: range.start,
    end: range.end,
    label: `Chapters ${range.start}–${range.end}`,
    html,
  };
}
