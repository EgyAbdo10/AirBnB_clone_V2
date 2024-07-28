#!/usr/bin/python3
"""this module creates starts a Flask web application"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def open_web():
    """open web and return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def open_web_2():
    """open web app on page hbnb and return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def get_c_text(text):
    """open web app on page c and print 'C <text>' """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def get_python_text(text="is_cool"):
    """open web app on page c and print 'python <text>' """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:num>", strict_slashes=False)
def get_num(num):
    """open web app on page and prints num is a number """
    return f"{num} is a number"


@app.route("/number_template/<int:num>", strict_slashes=False)
def get_num_html(num):
    """open web app on page and return an html file """
    return render_template("5-number.html", num=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
