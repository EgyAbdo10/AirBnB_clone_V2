#!/usr/bin/python3
"""create a flask app"""


from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    print("worked")
    storage.close()


@app.route("/states_list", strict_slashes=False)
def get_states():
    objs_dict = storage.all("State")
    print((storage))
    sorted_dict = dict(sorted(objs_dict.items(),
                              key=lambda item: (item[1].name, item[0])))
    return render_template("7-states_list.html", obj_vals=objs_dict.values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
