from http.server import *
from urllib.parse import urlparse
import json
import sys
import os
sys.path.append(os.path.dirname(__file__))
import data_processing



class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200) # Response 200 = OK
        self.send_header('Content-type', 'application/json') # MIME-TYPE = e.g. application/json
        self.end_headers()

        # Parse the request URL to get the parameters
        query = urlparse(self.path).query
        myDict = {}
        for qc in query.split('&'):
            arg_pair = qc.split("=")
            if len(arg_pair) < 2: continue # No argument pair detected
            myDict[arg_pair[0]] = arg_pair[1]

            # Do some processing of the data
            myDict = data_processing.PreprocessData(myDict)

        print(myDict)

        # Write to output / Send response
        self.wfile.write(bytes(json.dumps(myDict), 'utf-8'))

server = HTTPServer(("webserver.srcf.net", 8080), MyHandler)
print("Serving ...")
server.serve_forever()

