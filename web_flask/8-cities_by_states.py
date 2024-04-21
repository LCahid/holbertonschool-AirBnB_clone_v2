#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""
from flask import Flask, render_template
from models import storage

app = Flask("__name__", template_folder="web_flask/templates")


@app.route("/cities_by_states", strict_slashes=False)
def get_cities_by_state():
    """Displays an HTML page with a list of all states and related cities.

    States/cities are sorted by name.
    """
    return render_template("8-cities_by_states.html",
                           states=storage.all("State"))


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
