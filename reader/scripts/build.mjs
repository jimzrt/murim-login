import { spawnSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { copyFileSync, mkdirSync, readdirSync, writeFileSync } from "node:fs";
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
const offlinePage = `${base}offline/index.html`.replace(/\/{2,}/g, "/");

mkdirSync(publicDir, { recursive: true });
mkdirSync(assetsDir, { recursive: true });
copyFileSync(coverSrc, resolve(publicDir, "cover.jpg"));
copyFileSync(coverSrc, resolve(assetsDir, "cover.jpg"));

const env = {
  ...process.env,
  ASTRO_OUT_DIR: outDir,
  MURIM_ROOT: process.env.MURIM_ROOT || repoRoot,
};
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

// Hashed Astro bundles live in a durable runtime cache instead of the precache:
// the precache drops a previous build's files on update, which would leave
// pages cached under that build unable to boot offline. sw-assets.js seeds the
// current build's bundles on install and on activate prunes only bundles that
// neither this build nor any cached page still references.
const astroAssets = readdirSync(resolve(outDir, "_astro"))
  .filter((name) => /\.(?:js|css|woff2)$/.test(name))
  .map((name) => `${base}_astro/${name}`);
writeFileSync(
  resolve(outDir, "sw-assets.js"),
  `const ASSET_CACHE = "astro-assets";
const PAGE_CACHE = "pages";
const ASSETS = ${JSON.stringify(astroAssets)};

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(ASSET_CACHE).then(async (cache) => {
      const missing = [];
      for (const url of ASSETS) {
        if (!(await cache.match(url))) {
          missing.push(url);
        }
      }
      await cache.addAll(missing);
    }),
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      const keep = new Set(ASSETS.map((url) => new URL(url, self.location.href).href));
      const pages = await caches.open(PAGE_CACHE);
      for (const request of await pages.keys()) {
        const response = await pages.match(request);
        const html = response ? await response.text() : "";
        for (const match of html.matchAll(/["'(]([^"'()\\s]*\\/_astro\\/[^"'()\\s]+)/g)) {
          keep.add(new URL(match[1], request.url).href);
        }
      }
      const assets = await caches.open(ASSET_CACHE);
      for (const request of await assets.keys()) {
        if (!keep.has(request.url)) {
          await assets.delete(request);
        }
      }
    })().catch(() => {}),
  );
});
`,
);

const { count, size, warnings } = await generateSW({
  globDirectory: outDir,
  globPatterns: ["offline/**", "cover.jpg", "favicon.svg", "manifest.webmanifest"],
  swDest: resolve(outDir, "sw.js"),
  importScripts: ["sw-assets.js"],
  skipWaiting: true,
  clientsClaim: true,
  cleanupOutdatedCaches: true,
  sourcemap: false,
  // No navigateFallback: it would answer every navigation before NetworkFirst.
  // The offline page is served only when network and the pages cache both miss.
  runtimeCaching: [
    {
      urlPattern: /\/(?:web|api|auth|email|image|avatar|admin)(?:\/|$)/,
      handler: "NetworkOnly",
    },
    {
      urlPattern: /\/view-counts\/?$/,
      handler: "NetworkOnly",
    },
    {
      urlPattern: /\/chapters\.json$/,
      handler: "NetworkFirst",
      options: {
        cacheName: "catalog",
        networkTimeoutSeconds: 3,
        expiration: {
          maxEntries: 1,
          maxAgeSeconds: 60 * 60 * 24,
        },
      },
    },
    {
      // Full navigations plus ClientRouter's same-origin HTML fetches (directory URLs).
      urlPattern: ({ request, url, sameOrigin }) =>
        request.method === "GET" &&
        (request.mode === "navigate" ||
          (sameOrigin && request.destination === "" && url.pathname.endsWith("/"))),
      handler: "NetworkFirst",
      options: {
        cacheName: "pages",
        networkTimeoutSeconds: 4,
        matchOptions: { ignoreVary: true },
        expiration: {
          maxEntries: 150,
          maxAgeSeconds: 60 * 60 * 24 * 30,
        },
        precacheFallback: {
          fallbackURL: offlinePage,
        },
      },
    },
    {
      urlPattern: /\/_astro\//,
      handler: "CacheFirst",
      options: {
        // Pruned by sw-assets.js, not by age or count.
        cacheName: "astro-assets",
      },
    },
    {
      urlPattern: /\/pagefind\//,
      handler: "StaleWhileRevalidate",
      options: {
        cacheName: "pagefind",
        expiration: {
          maxEntries: 64,
          maxAgeSeconds: 60 * 60 * 24,
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
  ],
});

if (warnings.length) {
  for (const warning of warnings) {
    console.warn(warning);
  }
}
console.log(`Generated sw.js precaching ${count} files (${size} bytes)`);
