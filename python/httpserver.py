# -*- coding:utf-8 -*-
#!/usr/bin/python
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib
import logging
import sys
import json
import bookmaker

class S(SimpleHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        #self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_POST(self):
        # <--- Gets the size of data
        content_length = int(self.headers['Content-Length'])
        # <--- Gets the data itself
        post_data = self.rfile.read(content_length)
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(
            self.path), str(self.headers), post_data.decode("utf-8"))
        global data
        data = post_data.decode("utf-8")
        if data is not None:
            bookmaker.dealWithData(data)
        self._set_response()
        self.wfile.write("POST request for {}".format(
            self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=10086):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
