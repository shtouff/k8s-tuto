import os
import socket

from flask import Flask, jsonify
from requests import session


app = Flask('proxyworld')
app.helloworld = dict(
    host=os.environ.get('HELLOWORLD_SERVICE_HOST', 'localhost'),
    port=os.environ.get('HELLOWORLD_SERVICE_PORT', 5000),
)
app.requests = session()


@app.route('/')
def slash():
    return jsonify(
        **app.requests.get('http://{}:{}/'.format(
            app.helloworld['host'],
            app.helloworld['port'],
        )).json(),
        proxy=socket.gethostname(),
    )
