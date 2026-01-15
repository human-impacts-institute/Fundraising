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
  const resetLabel = () => {
    button.textContent = defaultLabel;
  };

  button.addEventListener("click", async () => {
    if (button.disabled) {
      return;
    }

    button.disabled = true;
    button.classList.add("is-loading");
    button.textContent = "Refreshing...";

    try {
      const response = await fetch(proxyUrl, { method: "POST" });

      if (!response.ok) {
        throw new Error(`Refresh failed: ${response.status}`);
      }

      button.textContent = "Queued";
    } catch (error) {
      button.classList.add("has-error");
      button.textContent = "Refresh failed";
      button.disabled = false;
      setTimeout(() => {
        button.classList.remove("has-error");
        resetLabel();
      }, 3000);
      return;
    }

    setTimeout(() => {
      button.classList.remove("is-loading");
      resetLabel();
      button.disabled = false;
    }, 3000);
  });
})();
