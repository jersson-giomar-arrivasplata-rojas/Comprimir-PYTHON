
import http.server
from http.server  import BaseHTTPRequestHandler, HTTPServer
import logging
import socketserver


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Title goes here.</title></head>")
        self.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        self.wfile.write("</body></html>")
        
def main():
        try:
            PORT = 8000

            Handler = http.server.SimpleHTTPRequestHandler

            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print("serving at port", PORT)
                httpd.serve_forever()

        except KeyboardInterrupt:
            print (" ^C entered, stopping web server....")

if __name__ == '__main__':
    main()

