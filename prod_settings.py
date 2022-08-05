""" Production Settings """
# default: use settings from main settings.py if not overwritten
from spotify.settings import *

import django_heroku
import os


DEBUG = False
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)
# adjust to the URL of your Heroku app
ALLOWED_HOSTS = ['agile-badlands-93718.herokuapp.com']

# Activate Django-Heroku.
django_heroku.settings(locals())