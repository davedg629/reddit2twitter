from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
manager = Manager(app)
basic_auth = BasicAuth(app)

from app import models, views, admin_views
from admin_views import admin
admin.init_app(app)
