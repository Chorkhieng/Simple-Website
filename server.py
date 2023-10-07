from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib

def server(url):
    decoded_url = urllib.parse.unquote(url)
    parsed_url = urllib.parse.urlparse(decoded_url)
    path = parsed_url.path

    if path == "/" or path == "/main":
        return open("index.html").read(), "text/html"
    elif path == "/contact":
        return open("links/info.html").read(), "text/html"
    elif path == "/projects":
        return open("links/projects.html").read(), "text/html"
    elif path == "/main/css":
        return open("styles.css").read(), "text/css"
    elif path == "/css":
        return open("links/style.css").read(), "text/css"
    elif path == "/resume":
        return open("links/resume.html").read(), "text/html"
    elif path == "/courses":
        return open("links/courses.html").read(), "text/html"
    elif path == "/angkor":
        return open("images/angkor.jpg", "rb").read(), "image/jpeg"
    elif path == "/beach":
        return open("images/beach.jpg", "rb").read(), "image/jpeg"
    elif path == "/maker_launch":
        return open("images/maker_launch.svg").read(), "image/svg+xml"
    elif path == "/sunset":
        return open("images/sunset.jpg", "rb").read(), "image/jpeg"
    elif path == "/panda":
        return open("images/Grosser_Panda.jpg", "rb").read(), "image/jpeg"
    else:
        return open("links/page_error/error.html").read(), "text/html"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Call the student-edited server code.
        message, content_type = server(self.path)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # prepare the response object with minimal viable headers.
        self.protocol_version = "HTTP/1.1"
        # Send response code
        self.send_response(200)
        # Send headers
        # Note -- this would be binary length, not string length
        self.send_header("Content-Length", len(message))
        self.send_header("Content-Type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)
        return

def run():
    PORT = 8000
    print(f"Starting server http://localhost:{PORT}/")
    server = ('', PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()
run()