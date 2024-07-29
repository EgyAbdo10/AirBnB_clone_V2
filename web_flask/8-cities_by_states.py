#!/usr/bin/python3
"""create a flask app"""


from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """cloas connection after every request"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def get_states():
    """ get all states objects and their cities"""
    states = storage.all("State").values()
    # sorted_states_dict = dict(sorted(states_dict.items(),
    #   key=lambda item: (item[1].name, item[0])))

    # cities = storage.all("City").values()
    # sorted_cities_dict = dict(sorted(cities_dict.items(),
    #   key=lambda item: (item[1].name, item[0])))
    return render_template("8-cities_by_states.html",
                           states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
