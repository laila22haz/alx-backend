#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get_local function"""
    return request.accept_languages.best_match(["LANGUAGES"])


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(debug=True)
