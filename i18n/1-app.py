#!/usr/bin/env python3
'''Basic Flask App'''
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    '''Configuration'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route("/")
def index():
    '''INDEX PAGE'''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
