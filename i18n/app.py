#!/usr/bin/env python3
"""Flask app with current time display"""
import pytz
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Determine best match language based on priority order"""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone():
    """Determine best match timezone based on priority order"""
    timezone = request.args.get("timezone")
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            return pytz.timezone(g.user.get("timezone")).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return "UTC"


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


def get_user():
    """Return user dictionary or None if not found"""
    login_as = request.args.get("login_as")
    if login_as is None:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """Execute before all other functions"""
    g.user = get_user()


@app.route("/")
def index():
    """Home page route"""
    timezone = get_timezone()
    tz = pytz.timezone(timezone)
    current_time = format_datetime(datetime.now(tz))
    return render_template("index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(debug=True)
