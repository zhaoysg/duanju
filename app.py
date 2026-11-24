import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def order_total_cents(items):
    return sum(items)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body, media = b'{"status":"ok"}', "application/json"
        elif self.path == "/api/summary":
            body = json.dumps({"total_cents": order_total_cents([199, 299])}).encode("utf-8")
            media = "application/json"
        elif self.path == "/":
            total = order_total_cents([199, 299])
            body = (f'<!doctype html><html lang="zh-CN"><meta charset="utf-8">'
                    f'<title>订单合计测试</title><style>body{{font:16px sans-serif;margin:60px;color:#172033}}'
                    f'main{{max-width:500px;padding:28px;border:1px solid #dbe3ef;border-radius:12px}}'
                    f'strong{{font-size:32px;color:#2563eb}}</style><main><h1>订单合计测试</h1>'
                    f'<p>合成测试商品金额为 199 分和 299 分。</p>'
                    f'<p>合计 <strong id="total">{total}</strong> 分</p></main></html>').encode("utf-8")
            media = "text/html; charset=utf-8"
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", media)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_args):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    with ThreadingHTTPServer(("127.0.0.1", args.port), Handler) as server:
        server.serve_forever()
