#!/usr/bin/env python3
'''
Flask-Babel is a flask extension that makes working
with translatoons very easy
install pip3 install flask-babel

'''

# initialize flask-babel as shown below

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)

#adding language translator

class Config(object):
    #languages
    LANGUAGES = ['en', 'es']

#the Babel module instance provides localeselector decorator
#decorated function invokes each request to selct a language translation to use for that request

from flask import request
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

#accept_languages is aa flask request attribute that 
#provides a high-level interface to work with the Accept-Language header
# that clients send with a request

#accept-language header

Accept-Language: da, en-gb; q = 0.8, en;q = 0.7

#the above shows that Danish(da) is the preferred language
#with default weight = 1.0, fpollowed by Broitish Eng(en-GB) is with 0.8 weight, and last option 
#generic English(en) with 0..7  weight
