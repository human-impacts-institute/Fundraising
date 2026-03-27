(() => {
  const button = document.querySelector(".refresh-button");
  if (!button) {
    return;
  }

  const proxyUrl = (window.REFRESH_PROXY_URL || "").trim();
  if (!proxyUrl) {
    button.disabled = true;
    button.title = "Configure REFRESH_PROXY_URL to enable refresh.";
    return;
  }

  const defaultLabel = button.textContent || "Refresh";

  // How long to wait (ms) before auto-reloading after a successful dispatch.
  // Covers ~23s workflow + ~15s Netlify deploy with some headroom.
  const RELOAD_AFTER_MS = 45_000;

  button.addEventListener("click", async () => {
    if (button.disabled) {
      return;
    }

    button.disabled = true;
    button.classList.add("is-loading");
    button.textContent = "Syncing…";

    try {
      const response = await fetch(proxyUrl, { method: "POST" });
      if (!response.ok) {
        throw new Error(`${response.status}`);
      }
    } catch (error) {
      button.classList.remove("is-loading");
      button.classList.add("has-error");
      button.textContent = "Refresh failed";
      setTimeout(() => {
        button.classList.remove("has-error");
        button.textContent = defaultLabel;
        button.disabled = false;
      }, 3000);
      return;
    }

    // Count up every second, then auto-reload when done.
    let elapsed = 0;
    const totalSecs = Math.round(RELOAD_AFTER_MS / 1000);

    const tick = setInterval(() => {
      elapsed++;
      if (elapsed >= totalSecs) {
        clearInterval(tick);
        window.location.reload();
      } else {
        button.textContent = `Syncing… ${elapsed}s`;
      }
    }, 1000);
  });
})();
