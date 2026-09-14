# Murim Login — English Translation

A consistent English translation of **Murim Login**, built from the Korean source and maintained as Markdown.

**Read online:** https://jimzrt.github.io/murim-login/
**PDF / EPUB:** https://github.com/jimzrt/murim-login/releases/tag/ebook

## Why this exists

Existing chapters of *Murim Login* are scattered around the web across multiple translation sources. Quality ranges from good to barely readable, and terminology, names, character voices, and formatting often change between chapters.

The goal of this project is not simply to machine-translate the novel again. It is to produce **one reasonably high-quality and, most importantly, consistent English edition**.

The translations live in [`translations/`](translations/) as ordinary Markdown files. They can therefore be reviewed, diffed, corrected, and improved through pull requests instead of being opaque generated output.

This is still a work in progress. The pipeline deliberately spends significantly more compute than a simple translation pass: a chapter currently requires a substantial token budget and roughly **30 minutes** to process.

## Translation workflow

The translation is controlled by a Python workflow rather than a single large prompt.

```mermaid
flowchart TD
    A[Korean source] --> B[Context builder]

    B --> B1[Translation rules]
    B --> B2[Terminology / names]
    B --> B3[Character profiles]
    B --> B4[Bounded continuity]
    B --> B5[Previous summaries]

    B --> C[Draft model]
    C --> D[Deterministic QA]

    D --> E[Independent review model]
    E --> F[Structured findings]
    F --> G[Deterministic exact-span revision]
    G --> H[Final QA]

    H --> I[Update names / continuity / summaries]
    I --> J[Mastering editor]

    J --> K[Paragraph-aware diff]
    K --> L[Independent adjudicator]
    L --> M[Assemble final chapter]
    M --> N[Final fidelity + deterministic QA]

    N --> O["translations/NNNN.md"]
```

The important part is that model output is **not accepted directly**.

The pipeline uses:

* a bounded context instead of feeding the complete novel into every request;
* a persistent terminology and names ledger;
* spoiler-safe character profiles and continuity state;
* explicit translation and style rules;
* a dedicated draft model and an independent review model;
* deterministic QA between stages;
* structured review findings with exact replacements rather than another uncontrolled rewrite;
* a separate mastering pass whose changes are diffed and independently adjudicated;
* hashes and transaction state so failed or stale runs stop instead of silently continuing.

The Python controller decides which stage is allowed to run next. The models translate and review; they do not control the workflow.

That does not make this human translation. It is still LLM-assisted translation. The difference is that consistency, terminology, continuity, review, and publication are treated as an engineering pipeline rather than as one prompt followed by `save output`.

## Architecture

```mermaid
flowchart LR
    S["source/<br/>Korean"] --> T["Python translation<br/>pipeline"]
    C["Rules / glossary /<br/>profiles / context"] --> T

    T --> M["translations/<br/>Markdown"]

    M --> W["Astro reader"]
    M --> P["Pandoc"]
    P --> E["EPUB"]
    P --> Y["Typst"]
    Y --> PDF["PDF"]

    W --> GH["GitHub Pages"]
    E --> R["GitHub Release"]
    PDF --> R
```

| Layer                      | Technology                  |
| -------------------------- | --------------------------- |
| Translation orchestration  | Python                      |
| Translation storage        | Markdown                    |
| Web reader                 | Astro, TypeScript / Node.js |
| EPUB generation            | Pandoc                      |
| PDF generation             | Pandoc + Typst              |
| Document filtering/styling | Lua, CSS, Typst             |
| CI / publication           | GitHub Actions              |

## Reader and releases

Markdown is the canonical format.

Every push to `master` automatically rebuilds and deploys the web reader through GitHub Actions. The reader supports chapter navigation, filtering, reading progress, configurable width/font size, light and dark themes, and related reading features.

A second workflow builds the complete translation as **PDF and EPUB** and updates a rolling GitHub release. The web version, EPUB, and PDF therefore all originate from the same translated Markdown.

```text
translations/*.md
       │
       ├──> Astro ─────────────> GitHub Pages
       │
       ├──> Pandoc ────────────> EPUB
       │
       └──> Pandoc + Typst ────> PDF
                                  │
                         rolling GitHub release
```

## Contributing

The final chapters are deliberately stored as Markdown rather than generated binaries.

If a translation is awkward, inconsistent, or wrong, open a pull request against the relevant file in [`translations/`](translations/). Improvements can then be reviewed as normal source changes and automatically propagate to the web, EPUB, and PDF editions.

The objective is not to claim that an automated pipeline produces a perfect translation. It is to maintain a **consistent, inspectable, and continuously improvable edition** of the novel.
