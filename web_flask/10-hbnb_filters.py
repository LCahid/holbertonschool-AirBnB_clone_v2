#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from flask import Flask, render_template
from models import storage

app = Flask("__name__", template_folder="web_flask/templates",
            static_folder="web_flask/static")


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Displays hbnb filters
    """
    states = storage.all("State").values()
    amentities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amentities)


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
