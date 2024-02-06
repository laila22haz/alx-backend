#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel


class Config(object):
    """config class"""
    LANGUAGES = ["en", "fr"]
    default_local = "en"
    default_zone = "UTC"

app.config.from_object(Config)

@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
