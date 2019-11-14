# -*- coding: UTF-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello World!'

@app.route('/health')
def readiness():
    return { 'status' : 'ready', 'app' : 'test' } , 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')