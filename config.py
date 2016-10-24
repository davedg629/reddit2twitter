import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# basic auth
BASIC_AUTH_FORCE = True
BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')

# twitter api
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_CALLBACK = os.environ.get('TWITTER_CALLBACK')
TWITTER_LINK_LEN = os.environ.get('TWITTER_LINK_LEN')
TWITTER_LINK_LEN_HTTPS = os.environ.get('TWITTER_LINK_LEN_HTTPS')

# set to 'heroku' if hosting with heroku
if os.environ.get('ENVIRONMENT') is None:
    ENVIRONMENT = 'dev'
else:
    ENVIRONMENT = os.environ.get('ENVIRONMENT')
    DEBUG = False

# flask secret key
if os.environ.get('SECRET_KEY') is None:
    SECRET_KEY = 'secret_key'
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')

# SQLALchemy database URI
if os.environ.get('DATABASE_URL') is None:
    DATABASE = 'reddit2twitter.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, DATABASE) + \
        '?check_same_thread=False'
else:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# reddit
if os.environ.get('REDDIT_UA') is None:
    REDDIT_USER_AGENT = "your app name ver 0.1 by /u/your_user_name, "\
        "https://github.com/davedg629/reddit2twitter"
else:
    REDDIT_USER_AGENT = os.environ.get('REDDIT_UA')

if os.environ.get('REDDIT_APP_ID') is None:
    REDDIT_APP_ID = 'reddit_app_id'
else:
    REDDIT_APP_ID = os.environ.get('REDDIT_APP_ID')

if os.environ.get('REDDIT_APP_SECRET') is None:
    REDDIT_APP_SECRET = 'reddit_app_secret'
else:
    REDDIT_APP_SECRET = os.environ.get('REDDIT_APP_SECRET')

if os.environ.get('OAUTH_REDIRECT_URI') is None:
    OAUTH_REDIRECT_URI = 'http://localhost:5000/authorize'
else:
    OAUTH_REDIRECT_URI = os.environ.get('OAUTH_REDIRECT_URI')

if os.environ.get('OAUTH_REFRESH_TOKEN') is None:
    OAUTH_REFRESH_TOKEN = 'http://localhost:5000/authorize'
else:
    OAUTH_REFRESH_TOKEN = os.environ.get('OAUTH_REFRESH_TOKEN')
