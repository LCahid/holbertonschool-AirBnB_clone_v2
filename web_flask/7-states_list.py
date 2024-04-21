#!/usr/bin/python3
"""
Starting Flask WEB application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

# Creating an instance of Flask class
app = Flask('__name__', template_folder="web_flask/templates")


@app.route("/states_list", strict_slashes=False)
def get_states():
    """get states"""
    states = storage.all(State).values()
    # print(states)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_storage(exception):
    """close storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
