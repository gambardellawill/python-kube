# -*- coding: UTF-8 -*-

from flask import Flask, Response, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello World!'

@app.route('/health')
def readiness():
    check = { 'status' : 'ready', 'app' : 'test' }
    return jsonify(check), 200

if __name__ == "__main__":
    app.run()