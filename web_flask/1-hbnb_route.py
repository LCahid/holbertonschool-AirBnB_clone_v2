#!/usr/bin/python3
'''Module for the flask application'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
