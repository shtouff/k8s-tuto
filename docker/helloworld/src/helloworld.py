import os

from flask import Flask, jsonify, request

app = Flask('helloworld')


@app.route('/')
def slash():
    return jsonify(
        message='hello world',
        server=os.environ.get('HOSTNAME'),
    )
