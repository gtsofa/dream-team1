

# app/__init__.py

# third-party imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

app = Flask(__name__)

# local imports
from instance.config import app_config

# db variable initialization
db = SQLAlchemy()

#create an object that will use the flask login class
login_manager = LoginManager()

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app



    
# temporary route
""""
@app.route('/')
def hello_world():
    return 'Hello, Tsofa !'
"""
    


"""
@app.route('/')
def hello_world():
    return render_template('hello.html')
"""