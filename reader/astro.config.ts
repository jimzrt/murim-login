import path from "node:path";
import { fileURLToPath } from "node:url";
import { defineConfig } from "astro/config";
import { satteri } from "@astrojs/markdown-satteri";
import sitemap from "@astrojs/sitemap";
import { systemWindows } from "./src/plugins/system-windows";

/** This file is `reader/astro.config.ts`; the translation repo is always its parent. */
const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
process.env.MURIM_ROOT ??= repoRoot;

function siteUrl(): string {
  return process.env.ASTRO_SITE ?? "https://murim-login.local";
}

function siteBase(): string {
  const raw = process.env.ASTRO_BASE ?? "/";
  if (!raw || raw === "/") {
    return "/";
  }
  return `/${raw.replace(/^\/+|\/+$/g, "")}/`;
}

export default defineConfig({
  site: siteUrl(),
  base: siteBase(),
  trailingSlash: "always",
  outDir: process.env.ASTRO_OUT_DIR ?? "../build/html",
  compressHTML: true,
  prefetch: true,
  redirects: {
    "/chapters/": "/",
  },
  build: {
    format: "directory",
  },
  vite: {
    define: {
      "import.meta.env.MURIM_ROOT": JSON.stringify(process.env.MURIM_ROOT || repoRoot),
    },
  },
  integrations: [sitemap()],
  markdown: {
    processor: satteri({
      hastPlugins: [systemWindows],
      features: {
        gfm: {
          footnotes: {
            backContent: "↩",
            backLabel: "Back to reference {reference}",
            label: "Footnotes",
          },
        },
      },
    }),
  },
});
