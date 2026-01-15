const json = (status, data, origin) =>
  new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": origin,
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    },
  });

export default {
  async fetch(request, env) {
    const origin = env.ALLOWED_ORIGIN || "*";

    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: {
          "Access-Control-Allow-Origin": origin,
          "Access-Control-Allow-Methods": "POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type",
          "Access-Control-Max-Age": "86400",
        },
      });
    }

    if (request.method !== "POST") {
      return json(405, { error: "Method Not Allowed" }, origin);
    }

    const owner = (env.OWNER || "").trim();
    const repo = (env.REPO || "").trim();
    const workflow = (env.WORKFLOW_FILE || "").trim();
    const ref = (env.WORKFLOW_REF || "main").trim();
    const token = (env.GITHUB_TOKEN || "").trim();

    if (!owner || !repo || !workflow || !token) {
      return json(500, { error: "Missing required configuration." }, origin);
    }

    const url = `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${workflow}/dispatches`;
    const response = await fetch(url, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        Accept: "application/vnd.github+json",
        "User-Agent": "fundraising-refresh-worker",
      },
      body: JSON.stringify({ ref }),
    });

    if (!response.ok) {
      return json(response.status, { error: "Dispatch failed." }, origin);
    }

    return json(202, { status: "queued" }, origin);
  },
};
