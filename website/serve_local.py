#!/usr/bin/env python3
"""Local preview server with Quartz clean-URL support (/page -> /page.html)."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import urllib.parse
import sys

ROOT = Path(__file__).resolve().parent / "public"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path):
        # decode %xx (Chinese filenames)
        path = urllib.parse.unquote(path)
        fs_path = super().translate_path(path)
        p = Path(fs_path)
        if p.exists():
            return fs_path
        # /name -> /name.html
        if not p.suffix:
            html = p.with_suffix(".html")
            if html.exists():
                return str(html)
            # /name -> /name/index.html
            index = p / "index.html"
            if index.exists():
                return str(index)
        return fs_path


if __name__ == "__main__":
    if not ROOT.exists():
        print(f"missing {ROOT}, run: npx quartz build -d ../Publish")
        sys.exit(1)
    print(f"Serving {ROOT}")
    print(f"Open http://127.0.0.1:{PORT}/")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
