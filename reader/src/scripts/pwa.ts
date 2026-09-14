const base = document.documentElement.getAttribute("data-base") || "/";
const swUrl = `${base.replace(/\/?$/, "/")}sw.js`;

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    void navigator.serviceWorker.register(swUrl, { scope: base }).catch(() => {
      /* private mode / unsupported */
    });
  });
}
