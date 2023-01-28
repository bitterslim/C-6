from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler

from core.static_responder import StaticResponder
from core.urls import router
from requests.request import Request
from requests.response import Response


class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        request = Request(self.rfile)
        response = Response(self.wfile)
        responder = StaticResponder(request, response)
        if responder.file:
            responder.prepare_response()
        else:
            router.run(request, response)
        response.add_header('Connection', 'close')
        response.send()


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass
