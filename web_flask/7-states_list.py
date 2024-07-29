#!/usr/bin/python3
"""create a flask app"""


from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def get_states():
    states_dict = storage.all("State")
    sorted_states_dict = dict(sorted(states_dict.items(),
                              key=lambda item: (item[1].name, item[0])))
    
    cities_dict = storage.all("City")
    sorted_cities_dict = dict(sorted(cities_dict.items(),
                              key=lambda item: (item[1].name, item[0])))
    return render_template("7-states_list.html",
                           states=sorted_states_dict.values(),
                           cities=sorted_cities_dict.values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
