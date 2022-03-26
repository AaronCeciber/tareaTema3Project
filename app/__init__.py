from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "ClaveSecreta"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tareaTema3Project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .public import public
from .private import private
from .login import login

def create_app():

    app.register_blueprint(public)
    app.register_blueprint(private)
    app.register_blueprint(login)
    return app