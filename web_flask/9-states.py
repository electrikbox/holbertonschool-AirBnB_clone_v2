#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", defaults={'id': None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list(id):
    """Displaylist of states sorted by name"""
    states = storage.all(State)
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def close_session(self):
    """ Closes the session after each request """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
