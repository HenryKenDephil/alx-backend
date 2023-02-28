#!/usr/bin/env python3
#Get locale from request

from flask import Flask, render_template
from flask_babel import Babel, request
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

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(app.config['LANGUAGES', 'us_date'])

    def index():
        return render_template('2-index.html', name = 'babel')
    

    if __name__ == '__main__':
        app.run(debug=True)