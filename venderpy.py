
##initial
# import http.server
# import socketserver

# PORT = 80

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

##changed
import http.server
import socketserver

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/vender.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        print(self.rfile.read(int(self.headers['Content-Length'])).decode("UTF-8"))
        content = "<h1> Thanks for letting us know!</h1>"
        self.path = 'realname','email','message'
        self.send_response(200)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Content-Length", len(content))
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content.encode(encoding = "utf_8")))

# print ("Listening on localhost:8080")
# Handler = MyRequestHandler
# server = socketserver.TCPServer(('0.0.0.0', 8080), Handler)
# server.serve_forever()


def main():
    try:
        print ("Listening on localhost:8080")
        Handler = MyRequestHandler
        server = socketserver.TCPServer(('0.0.0.0', 8080), Handler)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()
