export {};

const base = document.documentElement.getAttribute("data-base") || "/";
const swUrl = `${base.replace(/\/?$/, "/")}sw.js`;
const expectedScope = new URL(base, window.location.origin).href;
const UPDATE_CHECK_MS = 30 * 60 * 1000;

// Never reload the page someone is reading. When a deploy ships a new service
// worker it takes over silently; the next in-app navigation then becomes a full
// page load so old and new bundles never run side by side.
let updateReady = false;

document.addEventListener("astro:before-preparation", (event) => {
  if (!updateReady) {
    return;
  }
  const prep = event as Event & { to: URL; navigationType: string };
  event.preventDefault();
  if (prep.navigationType === "traverse") {
    location.replace(prep.to.href);
  } else {
    location.assign(prep.to.href);
  }
});

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    void (async () => {
      const regs = await navigator.serviceWorker.getRegistrations();
      await Promise.all(
        regs.map(async (reg) => {
          const script =
            reg.active?.scriptURL || reg.waiting?.scriptURL || reg.installing?.scriptURL || "";
          const staleScope = reg.scope !== expectedScope;
          const staleScript =
            script.length > 0 &&
            new URL(script).pathname !== new URL(swUrl, window.location.origin).pathname;
          if (staleScope || staleScript) {
            await reg.unregister();
          }
        }),
      );

      // The first claim on a fresh install is not an update.
      let controlled = Boolean(navigator.serviceWorker.controller);
      navigator.serviceWorker.addEventListener("controllerchange", () => {
        updateReady ||= controlled;
        controlled = true;
      });

      const registration = await navigator.serviceWorker.register(swUrl, {
        scope: base,
        updateViaCache: "none",
      });

      let lastCheck = Date.now();
      document.addEventListener("visibilitychange", () => {
        if (document.visibilityState === "visible" && Date.now() - lastCheck > UPDATE_CHECK_MS) {
          lastCheck = Date.now();
          void registration.update();
        }
      });
    })().catch(() => {
      /* private mode / unsupported */
    });
  });
}
