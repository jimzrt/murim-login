const base = document.documentElement.getAttribute("data-base") || "/";
const swUrl = `${base.replace(/\/?$/, "/")}sw.js`;
const expectedScope = new URL(base, window.location.origin).href;

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    void (async () => {
      const regs = await navigator.serviceWorker.getRegistrations();
      await Promise.all(
        regs.map(async (reg) => {
          const script =
            reg.active?.scriptURL || reg.waiting?.scriptURL || reg.installing?.scriptURL || "";
          const staleScope = reg.scope !== expectedScope;
          const staleScript = script.length > 0 && new URL(script).pathname !== new URL(swUrl, window.location.origin).pathname;
          if (staleScope || staleScript) {
            await reg.unregister();
          }
        }),
      );
      await navigator.serviceWorker.register(swUrl, { scope: base });
    })().catch(() => {
      /* private mode / unsupported */
    });
  });
}
