#!/usr/bin/env python
import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器已启动: http://localhost:{PORT}")
    print(f"按 Ctrl+C 停止服务器")
    httpd.serve_forever()
