from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from database import registrationservice, notificationservice
import json

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        request_path = self.path
        if request_path == "/notifications":
            # Send response with the notifications
            notificationservice.notify(self.headers)
        print("\n----- Request Start ----->\n")
        print(request_path)
        print(self.headers)
        print("<----- Request End -----\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")

    def do_POST(self):

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)
        if request_path == "/register":
            #
            print("Want to register something")
            request_headers = self.headers
            content_length = request_headers.getheaders('content-length')
            length = int(content_length[0]) if content_length else 0
            registerInfo = json.loads(self.rfile.read(length))
            print(registerInfo["username"])
            print(registerInfo["password"])
            # Do registration
            registrationservice.register(registerInfo)
            # Send request for verification

        print(request_headers)
        #print(self.rfile.read(length))
        print("<----- Request End -----\n")

        self.send_response(200)

    do_PUT = do_POST
    do_DELETE = do_GET

def main():
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n")
    (options, args) = parser.parse_args()
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()
