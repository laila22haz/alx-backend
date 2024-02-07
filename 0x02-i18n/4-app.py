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
    global current_local
    current_local = Config.LANGUAGES[0]
    var_url = request.args.get('locale')
    if var_url and var_url in Config.LANGUAGES:
        return var_url
    else:
        return request.accept_languages.best_match(["LANGUAGES"])


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run(debug=True)
