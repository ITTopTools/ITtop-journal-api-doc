"""Build a Cloudflare Worker mock server from anonymized example payloads."""

from __future__ import annotations

import json
from pathlib import Path

EXAMPLES_PATH = Path("data/examples/latest.json")
WORKER_PATH = Path("mock/worker.js")
API_PREFIX = "/api/v2"


def _render_worker(mock_payloads: dict[str, object]) -> str:
    mock_json = json.dumps(mock_payloads, ensure_ascii=False, indent=2)
    return f"""const MOCK = {mock_json};

const CORS_HEADERS = {{
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
  "Access-Control-Allow-Headers": "*",
  "Content-Type": "application/json; charset=utf-8",
}};

function normalizePath(pathname) {{
  if (pathname === "{API_PREFIX}") {{
    return "/";
  }}

  if (pathname.startsWith("{API_PREFIX}/")) {{
    return pathname.slice("{len(API_PREFIX)}");
  }}

  return pathname;
}}

function jsonResponse(body, status = 200) {{
  return new Response(JSON.stringify(body), {{
    status,
    headers: CORS_HEADERS,
  }});
}}

export default {{
  async fetch(request) {{
    if (request.method === "OPTIONS") {{
      return new Response(null, {{
        status: 204,
        headers: CORS_HEADERS,
      }});
    }}

    const url = new URL(request.url);
    const normalizedPath = normalizePath(url.pathname);
    const payload = MOCK[normalizedPath];

    if (payload === undefined) {{
      return jsonResponse({{ error: "Not found", path: normalizedPath }}, 404);
    }}

    return jsonResponse(payload);
  }},
}};
"""


def main() -> int:
    examples = json.loads(EXAMPLES_PATH.read_text(encoding="utf-8"))
    WORKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    WORKER_PATH.write_text(_render_worker(examples), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
