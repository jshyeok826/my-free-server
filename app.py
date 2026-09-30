from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"<h1> 가상 컴퓨터 정상 작동 중! </h1><p>코드가 성공적으로 배포되었습니다.</p>")

port = int(os.environ.get("PORT", 8080))
server = HTTPServer(('0.0.0.0', port), MyHandler)
print(f"서버가 {port} 포트에서 시작되었습니다.")
server.serve_forever()
