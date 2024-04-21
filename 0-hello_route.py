#!/usr/bin/python3
"""
Starting Flask WEB application
"""
from flask import Flask

# Creating an instance of Flask class
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """Hello world in Flask"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
