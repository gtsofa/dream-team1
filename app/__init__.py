

# app/__init__.py

# third-party imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# local imports
from instance.config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
# temporary route
@app.route('/')
def hello_world():
    return 'Hello, Tsofa !'
    
    
    
        
    #return app
    


"""
@app.route('/')
def hello_world():
    return render_template('hello.html')
"""