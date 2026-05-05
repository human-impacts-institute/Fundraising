(() => {
  // -------------------------------------------------------
  // Part 1: Deadline countdown fill-in
  // -------------------------------------------------------
  function fillCountdowns() {
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    document.querySelectorAll("td.col-days[data-deadline]").forEach((cell) => {
      const raw = cell.dataset.deadline; // "YYYY-MM-DD"
      if (!raw) return;

      // Split manually to avoid UTC-midnight off-by-one in negative-UTC timezones
      const parts = raw.split("-");
      if (parts.length !== 3) return;
      const deadline = new Date(
        parseInt(parts[0], 10),
        parseInt(parts[1], 10) - 1,
        parseInt(parts[2], 10)
      );
      deadline.setHours(0, 0, 0, 0);

      const diffDays = Math.round((deadline - today) / (1000 * 60 * 60 * 24));

      let label, cls;
      if (diffDays < 0) {
        label = "OVERDUE";
        cls   = "deadline-overdue";
      } else if (diffDays === 0) {
        label = "today";
        cls   = "deadline-red";
      } else if (diffDays <= 30) {
        label = `in ${diffDays}d`;
        cls   = "deadline-red";
      } else if (diffDays <= 60) {
        label = `in ${diffDays}d`;
        cls   = "deadline-orange";
      } else {
        label = `in ${diffDays}d`;
        cls   = "deadline-green";
      }

      cell.textContent = label;
      cell.classList.add(cls);
    });
  }

  // -------------------------------------------------------
  // Part 2: Quick-add form toggle
  // -------------------------------------------------------
  function initFormToggle() {
    const toggle = document.querySelector(".grant-add-toggle");
    const form   = document.getElementById("grant-add-form");
    if (!toggle || !form) return;

    toggle.addEventListener("click", () => {
      const opening = form.hidden;
      form.hidden = !opening;
      toggle.setAttribute("aria-expanded", String(opening));
      if (opening) {
        form.querySelector("input, select, textarea")?.focus();
      }
    });
  }

  // -------------------------------------------------------
  // Part 3: Quick-add form submission
  // -------------------------------------------------------
  function initFormSubmit() {
    const form = document.getElementById("grant-add-form");
    if (!form) return;

    const addUrl = (window.GRANT_ADD_URL || "").trim();

    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const statusEl  = form.querySelector(".form-status");
      const submitBtn = form.querySelector(".form-submit");

      if (!addUrl) {
        if (statusEl) {
          statusEl.textContent = "Not configured. Set window.GRANT_ADD_URL in refresh-config.js.";
          statusEl.className   = "form-status form-status--error";
        }
        return;
      }

      const data = {
        org:         (form.querySelector("#ga-org")?.value          ?? "").trim(),
        infoUrl:     (form.querySelector("#ga-info-url")?.value     ?? "").trim(),
        appDeadline: (form.querySelector("#ga-app-deadline")?.value ?? "").trim(),
        loiDeadline: (form.querySelector("#ga-loi-deadline")?.value ?? "").trim(),
        priority:    (form.querySelector("#ga-priority")?.value     ?? ""),
        notes:       (form.querySelector("#ga-notes")?.value        ?? "").trim(),
      };

      if (!data.org) {
        form.querySelector("#ga-org")?.focus();
        return;
      }

      submitBtn.disabled = true;
      if (statusEl) {
        statusEl.textContent = "Saving...";
        statusEl.className   = "form-status";
      }

      try {
        await fetch(addUrl, {
          method:  "POST",
          mode:    "no-cors",
          headers: { "Content-Type": "text/plain" },
          body:    JSON.stringify(data),
        });
        // no-cors returns an opaque response — assume success if fetch resolves

        if (statusEl) {
          statusEl.textContent = "Added! Hit Refresh to update the dashboard.";
          statusEl.className   = "form-status form-status--success";
        }
        form.reset();

        setTimeout(() => {
          const t = document.querySelector(".grant-add-toggle");
          const f = document.getElementById("grant-add-form");
          if (t && f) { f.hidden = true; t.setAttribute("aria-expanded", "false"); }
          if (statusEl) statusEl.textContent = "";
        }, 4000);

      } catch (err) {
        if (statusEl) {
          statusEl.textContent = "Error saving. Please try again.";
          statusEl.className   = "form-status form-status--error";
        }
      } finally {
        submitBtn.disabled = false;
      }
    });
  }

  // -------------------------------------------------------
  // Init
  // -------------------------------------------------------
  function init() {
    fillCountdowns();
    initFormToggle();
    initFormSubmit();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
