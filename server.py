import BaseHTTPServer as http

class Handler(http.BaseHTTPRequestHandler):
  def do_GET(self):
		self.send_response(200)
		self.send_header('Content-Type', 'text/plain')
    self.send_headers()
    self.wfile.write("%s: I am alive!!!\n" % platfrom.node())
 		
if __name__ == '__main__':
  httpd = http.HTTPServer(('',8080),Handler)
  httpd.server_forever()
