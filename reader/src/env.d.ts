/// <reference types="astro/client" />

interface ImportMetaEnv {
  readonly PUBLIC_REPORT_LINE_URL?: string;
}

declare namespace astroHTML.JSX {
  interface IntrinsicElements {
    "pagefind-modal-trigger": astroHTML.JSX.HTMLAttributes;
    "pagefind-modal": astroHTML.JSX.HTMLAttributes;
    "pagefind-config": astroHTML.JSX.HTMLAttributes;
  }
}
