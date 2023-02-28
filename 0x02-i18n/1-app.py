#!/usr/bin/env python3
# Basic babel setup

from flask import Flask, render_template, request
from flask_babel import Babel
from datetime import datetime
from babel import dates 
from babel.dates import format_date

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

class Config(object):
    LANGUAGES = ['en', 'fr']
    d = datetime.utcnow()
    us_date = dates.format_date(d, locale = 'en')

    def index():
        return render_template('1-index.html', name = 'babel')
    

    if __name__ == '__main__':
        app.run(debug=True)