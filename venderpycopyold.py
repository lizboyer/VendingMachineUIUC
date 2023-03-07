
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
        return http.server.SimpleHTTPRequestHandler.do_POST(self)

Handler = MyRequestHandler
server = socketserver.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()




# def main():
#     try:
#         port = 8080
#         server = HTTPServer(('', port), WebServerHandler)
#         print ("Web Server running on port: 8080")
#         server.serve_forever()
#     except KeyboardInterrupt:
#         print (" ^C entered, stopping web server....")
#         server.socket.close()

# if __name__ == '__main__':
#     main()