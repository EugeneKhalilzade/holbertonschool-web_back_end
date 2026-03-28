#!/usr/bin/env python3
"""Flask app with Babel i18n support"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Determine best match language from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Home page route"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
