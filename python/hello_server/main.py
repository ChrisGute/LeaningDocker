'''
Tilte: hello_server
Version: 1.0.1
Owner: Chris Gutekanst
git: 
Description: Simple web server that counts the times that it has been request along
             with the details about the client.
'''
from flask import Flask
from flask import request
from waitress import serve
import logging
import time

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

def get_request_data():
    data = 'Headers:{}\nYour IP:{}\n'.format(request.headers, request.remote_addr)
    return data

# Log the request after we have the response payload
@app.after_request
def log_the_request(resp):
    msg = '{} {} {} {} {}'.format(
        time.time(),
        request.remote_addr,
        request.host,
        request.path,
        resp.status_code,

    )
    app.logger.info(msg)
    return resp

@app.route('/')
def say_hellow():
    return ('Hello User! Here is your info\n\n{}'.format(
        get_request_data()
    ))

if __name__ == '__main__':
    serve(app, listen='*:80')