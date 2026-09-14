import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const readerDir = join(dirname(fileURLToPath(import.meta.url)), "..");
const repoRoot = join(readerDir, "..");
const publicDir = join(readerDir, "public");
const assetsDir = join(readerDir, "src", "assets");
const coverSrc = join(repoRoot, "cover.jpg");

mkdirSync(publicDir, { recursive: true });
mkdirSync(assetsDir, { recursive: true });
copyFileSync(coverSrc, join(publicDir, "cover.jpg"));
copyFileSync(coverSrc, join(assetsDir, "cover.jpg"));
