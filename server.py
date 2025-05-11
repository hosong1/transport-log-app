import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# 🔥 핵심: 현재 파일(server.py)의 경로로 이동 (HTML 찾기용)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

# 브라우저 자동 실행
webbrowser.open(f"http://localhost:{PORT}/login.html")

# 서버 실행
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
