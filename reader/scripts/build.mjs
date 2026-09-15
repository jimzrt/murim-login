import { spawnSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { copyFileSync, mkdirSync, writeFileSync } from "node:fs";
import { generateSW } from "workbox-build";

const readerDir = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const repoRoot = resolve(readerDir, "..");
const outDir = resolve(process.env.ASTRO_OUT_DIR || resolve(repoRoot, "build/html"));
const publicDir = resolve(readerDir, "public");
const assetsDir = resolve(readerDir, "src", "assets");
const coverSrc = resolve(repoRoot, "cover.jpg");

function siteBase() {
  const raw = process.env.ASTRO_BASE ?? "/";
  if (!raw || raw === "/") {
    return "/";
  }
  return `/${raw.replace(/^\/+|\/+$/g, "")}/`;
}

const base = siteBase();
const offlinePath = `${base}offline/`.replace(/\/{2,}/g, "/");

mkdirSync(publicDir, { recursive: true });
mkdirSync(assetsDir, { recursive: true });
copyFileSync(coverSrc, resolve(publicDir, "cover.jpg"));
copyFileSync(coverSrc, resolve(assetsDir, "cover.jpg"));

const env = { ...process.env, ASTRO_OUT_DIR: outDir };
const bin = (name) => resolve(readerDir, "node_modules", ".bin", name);

function run(command, args) {
  const result = spawnSync(command, args, { cwd: readerDir, stdio: "inherit", env });
  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}

run(bin("astro"), ["build"]);
run(bin("pagefind"), ["--site", outDir]);

writeFileSync(
  resolve(outDir, "manifest.webmanifest"),
  JSON.stringify(
    {
      name: "Murim Login",
      short_name: "Murim Login",
      description: "A translation of the web novel Murim Login.",
      theme_color: "#f3ead4",
      background_color: "#f3ead4",
      display: "standalone",
      lang: "en",
      start_url: base,
      scope: base,
      icons: [
        {
          src: `${base}favicon.svg`.replace(/\/{2,}/g, "/"),
          sizes: "any",
          type: "image/svg+xml",
          purpose: "any",
        },
        {
          src: `${base}cover.jpg`.replace(/\/{2,}/g, "/"),
          sizes: "720x970",
          type: "image/jpeg",
          purpose: "any",
        },
      ],
    },
    null,
    2,
  ),
);

const { count, size, warnings } = await generateSW({
  globDirectory: outDir,
  globPatterns: [
    "**/*.{js,css,html,ico,svg,png,jpg,jpeg,webp,avif,woff2,json,webmanifest}",
    "pagefind/**/*",
  ],
  swDest: resolve(outDir, "sw.js"),
  navigateFallback: offlinePath,
  navigateFallbackDenylist: [
    /\/pagefind\//,
    /\/web(?:\/|$)/,
    /\/api(?:\/|$)/,
    /\/auth(?:\/|$)/,
    /\/email(?:\/|$)/,
    /\/image(?:\/|$)/,
    /\/avatar(?:\/|$)/,
    /\/admin(?:\/|$)/,
  ],
  skipWaiting: true,
  clientsClaim: true,
  sourcemap: false,
  runtimeCaching: [
    {
      urlPattern: /\/(?:web|api|auth|email|image|avatar|admin)(?:\/|$)/,
      handler: "NetworkOnly",
    },
    {
      urlPattern: ({ request }) => request.mode === "navigate",
      handler: "NetworkFirst",
      options: {
        cacheName: "pages",
        networkTimeoutSeconds: 4,
        expiration: {
          maxEntries: 80,
          maxAgeSeconds: 60 * 60 * 24 * 14,
        },
      },
    },
    {
      urlPattern: /\/_astro\//,
      handler: "CacheFirst",
      options: {
        cacheName: "astro-assets",
        expiration: {
          maxEntries: 128,
          maxAgeSeconds: 60 * 60 * 24 * 365,
        },
      },
    },
    {
      urlPattern: /\/pagefind\//,
      handler: "CacheFirst",
      options: {
        cacheName: "pagefind",
        expiration: {
          maxEntries: 64,
          maxAgeSeconds: 60 * 60 * 24 * 30,
        },
      },
    },
    {
      urlPattern: /\.(?:png|jpg|jpeg|svg|gif|webp|avif)$/i,
      handler: "CacheFirst",
      options: {
        cacheName: "images",
        expiration: {
          maxEntries: 64,
          maxAgeSeconds: 60 * 60 * 24 * 30,
        },
      },
    },
    {
      urlPattern: /\/chapters\.json$/,
      handler: "StaleWhileRevalidate",
      options: {
        cacheName: "catalog",
      },
    },
  ],
});

if (warnings.length) {
  for (const warning of warnings) {
    console.warn(warning);
  }
}
console.log(`Generated sw.js precaching ${count} files (${size} bytes)`);
