from http.server import HTTPServer, BaseHTTPRequestHandler
import concurrent.futures

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write("aaaa".encode('UTF-8'))

class Base:
    def __init__(self):
        print("init")

    def __listen(self):
        host = '0.0.0.0'
        port = 50001
        server = HTTPServer((host, port), Handler)

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        server.server_close()

    def start_listen(self):
        print("start_listen")
        self.__listen()
        #executer = concurrent.futures.ThreadPoolExecutor(max_workers = 2)
        #executer.submit(Base.__listen)

if __name__ == "__main__":
    base = Base()
    base.start_listen()
