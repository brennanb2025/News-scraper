import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'th1515453cr3tk37'
    #generates a hidden field that includes a token that is used to protect the form against CSRF attacks
    