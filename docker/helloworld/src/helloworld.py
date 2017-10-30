import socket

from flask import Flask, jsonify

app = Flask('helloworld')


@app.route('/')
def slash():
    return jsonify(
        message='hello world',
        server=socket.gethostname(),
    )
