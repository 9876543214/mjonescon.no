"""Preview the site locally: serves docs/ the way GitHub Pages does (right file types, 404.html for missing pages).

    python tools/serve.py [port]       (default 8000), then open http://127.0.0.1:<port>/
"""

import http.server
import mimetypes
import sys
from functools import partial
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

# Windows takes file types from the registry, which often lacks these
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("text/css", ".css")


class Handler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        page = DOCS / "404.html"
        if code == 404 and page.exists():
            body = page.read_bytes()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    handler = partial(Handler, directory=str(DOCS))
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as server:
        print(f"http://127.0.0.1:{port}/")
        server.serve_forever()


if __name__ == "__main__":
    main()
