# Date : 17 - 08 - 2022
# Ref: RFTM v2
'''
Python3 simple-https-server.py
'''

import http.server, ssl, socketserver

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("cert.pem") # PUT YOUR cert.pem HERE
server_address = ("192.168.43.210", 4443)  # CHANGE THIS IP & PORT

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(server_address, handler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()
