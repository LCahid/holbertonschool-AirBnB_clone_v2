#!/usr/bin/python3
'''Module for the flask application'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    states = storage.all(State).values()
    if id:
        for state in states:
            if state.id == id:
                states = state
                break
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
