from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy
from logs.logs import configure_logging

app = Flask(__name__)
app.secret_key = "ClaveSecreta"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tareaTema3Project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = "login.login"

logger = configure_logging(__name__)

app.config["RECAPTCHA_SITE_KEY"] = "6LddRD0fAAAAAJ-Q0kITeWqDTEodL1-HCTu4fs0-"
app.config["RECAPTCHA_SECRET_KEY"] = "6LddRD0fAAAAAGxYZX6FVxi6Pobq-g_Ju1QvABm8"
recaptcha = ReCaptcha(app)

from .public import public
from .private import private
from .login import login
from .admin import admin

def create_app():

    app.register_blueprint(public)
    app.register_blueprint(private)
    app.register_blueprint(login)
    app.register_blueprint(admin)
    return app