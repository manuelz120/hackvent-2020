#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000

SimpleHTTPRequestHandler.extensions_map = { k: v + ';charset=UTF-8' for k, v in SimpleHTTPRequestHandler.extensions_map.items() }
handler = SimpleHTTPRequestHandler

with TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))

    httpd.serve_forever()