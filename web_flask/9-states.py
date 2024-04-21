#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from flask import Flask, render_template
from models import storage

app = Flask("__name__", template_folder="web_flask/templates")


@app.route("/states", strict_slashes=False)
def get_states():
    """Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    return render_template("9-states.html", states=storage.all("State"))


@app.route("/states/<id>", strict_slashes=False)
def get_state(id):
    """Displays an HTML page with info about <id>, if it exists."""
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", states=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
