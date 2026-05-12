#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080

# 切换到脚本所在目录，确保能正确提供文件
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class ReusableTCPServer(socketserver.TCPServer):
    """允许端口快速复用，避免 TIME_WAIT 导致绑定失败"""
    allow_reuse_address = True

Handler = http.server.SimpleHTTPRequestHandler

while True:
    try:
        with ReusableTCPServer(("", PORT), Handler) as httpd:
            print(f"✅ 服务器已启动 → http://localhost:{PORT}")
            webbrowser.open(f"http://localhost:{PORT}")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n🛑 正在关闭服务器...")
                httpd.server_close()
                print("✔️ 服务器已关闭，端口已释放。")
                sys.exit(0)
    except OSError as e:
        # Windows errno 10048: Address already in use
        if e.errno in (10048, 98, 48):
            print(f"⚠️ 端口 {PORT} 被占用，尝试 {PORT+1} …")
            PORT += 1
        else:
            raise