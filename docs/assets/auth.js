(() => {
  const ALLOWED = "@humanimpactsinstitute.org";

  const gate    = document.getElementById("auth-gate");
  const content = document.getElementById("auth-content");
  const errEl   = document.getElementById("auth-error");
  const loginBtn = document.getElementById("auth-login-btn");

  loginBtn?.addEventListener("click", () => netlifyIdentity.open("login"));

  function apply(user) {
    if (!user) {
      gate.hidden    = false;
      content.hidden = true;
      if (errEl) errEl.hidden = true;
      return;
    }

    if (!user.email.toLowerCase().endsWith(ALLOWED)) {
      netlifyIdentity.logout();
      if (errEl) {
        errEl.textContent = "Access is restricted to @humanimpactsinstitute.org accounts.";
        errEl.hidden = false;
      }
      gate.hidden    = false;
      content.hidden = true;
      return;
    }

    gate.hidden    = true;
    content.hidden = false;
    window.scrollTo(0, 0);
    addSignOutButton(user);
  }

  function addSignOutButton(user) {
    if (document.getElementById("auth-signout")) return;
    const meta = document.querySelector(".dashboard-meta");
    if (!meta) return;
    const btn = document.createElement("button");
    btn.id        = "auth-signout";
    btn.className = "auth-signout-btn";
    btn.title     = "Sign out";
    btn.textContent = user.email;
    btn.addEventListener("click", () => netlifyIdentity.logout());
    meta.prepend(btn);
  }

  netlifyIdentity.on("init",   user => apply(user));
  netlifyIdentity.on("login",  user => { netlifyIdentity.close(); apply(user); });
  netlifyIdentity.on("logout", ()   => apply(null));
})();
