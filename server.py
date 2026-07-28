import http.server
import socketserver
import os

os.chdir("/storage/emulated/0/CODE/斗地主")

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        with open("斗地主.html", "rb") as f:
            self.wfile.write(f.read())
    def log_message(self, fmt, *args):
        pass

with socketserver.TCPServer(("127.0.0.1", 9090), Handler) as httpd:
    httpd.serve_forever()
