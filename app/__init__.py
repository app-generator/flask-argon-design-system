# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask            import Flask
from flask_bootstrap  import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login      import LoginManager
from flask_bcrypt     import Bcrypt
from flask_mail       import Mail


# load RES
from . data import Data  

app = Flask(__name__, static_url_path='/static')

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('app.configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')

# Expose globals to Jinja2 templates
app.add_template_global( app.config , 'cfg'  )
app.add_template_global( Data       , 'data' )

db   = SQLAlchemy  (app) #flask-sqlalchemy
lm   = LoginManager(   ) #flask-loginmanager
bc   = Bcrypt      (app) #flask-bcrypt

lm.init_app(app) # init the login manager

from app import views, models
