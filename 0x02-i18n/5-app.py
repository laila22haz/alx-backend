#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, g, request
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get_user function"""
    user_id = request.args.get('login_as')
    if user_id is not None:
        user_id = int(user_id)
        return users.get(user_id)
    else:
        return None


@app.before_request
def before_request():
    """before_request funtion"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return render_template("5-index.html")


if __name__ == '__main__':
    app.run(debug=True)
