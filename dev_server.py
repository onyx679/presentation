from __future__ import annotations

import io
import os
import shutil
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
REMOTE_ORIGIN = "https://app.spline.design"
LOCAL_VIEWER_ROUTE = "/file/b5699b21-c899-49e4-93ea-c50ffc534501"
LOCAL_VIEWER_FILE = ROOT / "public" / "nexbot-viewer.html"
PROXY_PREFIXES = (
    "/assets/",
    "/_assets/",
    "/_libraries/",
    "/_vercel/",
    "/api/",
)


class PresentationHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self) -> None:
        if self._is_local_viewer():
            self._serve_local_viewer()
            return
        if self._should_proxy():
            self._proxy("GET")
            return
        super().do_GET()

    def do_HEAD(self) -> None:
        if self._is_local_viewer():
            self._serve_local_viewer(head_only=True)
            return
        if self._should_proxy():
            self._proxy("HEAD")
            return
        super().do_HEAD()

    def do_POST(self) -> None:
        if self._should_proxy():
            self._proxy("POST")
            return
        self.send_error(405, "Method Not Allowed")

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def log_message(self, format: str, *args) -> None:
        print("%s - - [%s] %s" % (self.address_string(), self.log_date_time_string(), format % args))

    def _should_proxy(self) -> bool:
        path = urlsplit(self.path).path
        return path.startswith(PROXY_PREFIXES)

    def _is_local_viewer(self) -> bool:
        path = urlsplit(self.path).path
        return path == LOCAL_VIEWER_ROUTE

    def _serve_local_viewer(self, head_only: bool = False) -> None:
        payload = LOCAL_VIEWER_FILE.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if not head_only:
            self.wfile.write(payload)

    def _proxy(self, method: str) -> None:
        target = REMOTE_ORIGIN + self.path
        body = None
        if method == "POST":
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length) if length > 0 else None

        headers = {
            "User-Agent": self.headers.get("User-Agent", "Mozilla/5.0"),
            "Accept": self.headers.get("Accept", "*/*"),
        }
        if self.headers.get("Content-Type"):
            headers["Content-Type"] = self.headers["Content-Type"]

        request = Request(target, data=body, headers=headers, method=method)

        try:
            with urlopen(request) as response:
                self.send_response(response.status)
                for key, value in response.headers.items():
                    lower = key.lower()
                    if lower in {
                        "connection",
                        "content-security-policy",
                        "content-security-policy-report-only",
                        "content-length",
                        "keep-alive",
                        "proxy-authenticate",
                        "proxy-authorization",
                        "te",
                        "trailers",
                        "transfer-encoding",
                        "upgrade",
                    }:
                        continue
                    self.send_header(key, value)
                payload = response.read()
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                if method != "HEAD":
                    self.wfile.write(payload)
        except HTTPError as exc:
            payload = exc.read()
            self.send_response(exc.code)
            self.send_header("Content-Type", exc.headers.get_content_type() or "text/plain")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            if method != "HEAD":
                self.wfile.write(payload)
        except URLError as exc:
            payload = f"Proxy error: {exc}".encode("utf-8")
            self.send_response(502)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            if method != "HEAD":
                self.wfile.write(payload)


def main() -> None:
    port = int(os.environ.get("PORT", "4174"))
    server = ThreadingHTTPServer(("127.0.0.1", port), PresentationHandler)
    print(f"Serving presentation on http://127.0.0.1:{port}/")
    server.serve_forever()


if __name__ == "__main__":
    main()
