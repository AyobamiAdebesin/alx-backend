#!/usr/bin/env python3
""" A basic Flask app """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Index page """
    return render_template('0-index.html')
