from flask import Flask

app = Flask('helloworld')

@app.route('/')
def slash():
    return 'OK', 200


