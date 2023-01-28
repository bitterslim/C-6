from socketserver import TCPServer

from core.server import ThreadedTCPServer, MyTCPHandler

HOST, PORT = "localhost", 8000
TCPServer.allow_reuse_address = True
with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()