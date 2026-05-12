#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.server
import socketserver
import os
import webbrowser
import threading
import time

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def open_browser():
    time.sleep(1.5)
    url = f"http://localhost:{PORT}/website.html"
    print(f"正在打开浏览器: {url}")
    webbrowser.open(url)

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 50)
    print("   网站聚合页 - 本地服务器")
    print("=" * 50)
    print()
    print(f"服务器地址: http://localhost:{PORT}")
    print(f"网页地址: http://localhost:{PORT}/website.html")
    print()
    print("按 Ctrl+C 停止服务器")
    print()
    
    threading.Thread(target=open_browser, daemon=True).start()
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"服务器已启动，正在运行...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print()
            print("服务器已停止")

if __name__ == "__main__":
    main()
