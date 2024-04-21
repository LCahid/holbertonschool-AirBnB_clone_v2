#!/usr/bin/python3
"""
Starting Flask WEB application
"""
from flask import Flask


# Creating an instance of Flask class
app = Flask('__name__')


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """Hello world in Flask"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb() -> str:
    """Returning HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Returning text"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    """Returning text"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def nums(n):
    """Working with numbers"""
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
