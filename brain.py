from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class AIRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/ai":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            data = json.loads(body.decode("utf-8"))

            print("Minecraftから受信:")
            print(data)

            response = {
                "message": "……受信しました。",
                "decision": "observe"
            }

            output = json.dumps(response, ensure_ascii=False).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(output)))
            self.end_headers()
            self.wfile.write(output)

        except Exception as e:
            print("エラー:", e)

            self.send_response(400)
            self.end_headers()

    def log_message(self, format, *args):
        return


def main():
    server = HTTPServer(("127.0.0.1", 8765), AIRequestHandler)

    print("紫識AI Pythonサーバー起動")
    print("http://127.0.0.1:8765/ai")

    server.serve_forever()


if __name__ == "__main__":
    main()
