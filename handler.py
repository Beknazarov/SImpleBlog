# coding: utf-8
from http.server import BaseHTTPRequestHandler

from method import HTTP_METHODS
from router import Router
from urls import patterns


class MyHandler(BaseHTTPRequestHandler):
    HTTP_METHODS = None

    def __init__(self, request, client_address, server):
        self.router = Router()
        self.router.register_routes(patterns)
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.HTTP_METHODS = HTTP_METHODS.GET
        self.router.handle(request=self)
        return

    def do_POST(self):
        self.HTTP_METHODS = HTTP_METHODS.POST
        self.router.handle(request=self)
        return

    def do_HEAD(self):
        pass

    def do_PUT(self):
        pass
