#!/usr/bin/env python3
'''Basic Flask App'''
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    '''Configuration'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    '''Get local'''
    return request.accept_languages.best_match(Config.LANGUAGES)


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    '''INDEX PAGE'''
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
