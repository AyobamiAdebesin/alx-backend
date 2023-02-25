#!/usr/bin/env python3
""" A basic Flask app """
from flask import Flask
from flask import render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app, default_locale='en', default_timezone='UTC')


@app.route("/", strict_slashes=False)
def index():
    """ Index page """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
