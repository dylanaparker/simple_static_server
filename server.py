import SimpleHTTPServer
import SocketServer

PORT = 3000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving site at port 3000"
httpd.serve_forever()
