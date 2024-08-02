#!/usr/bin/python3
"""create a flask app that gets data from a db or a file storage"""


from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """cloas connection after every request"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def get_cities_of_state():
    """ get all city objects of a state"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
