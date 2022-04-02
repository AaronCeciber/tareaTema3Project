from flask import render_template
from . import public
# from flask import request
# from ..login.forms import LoginForm
from .. import app


@public.route('/')
def index():  # put application's code here
    app.logger.debug("Entro por /")
    return render_template('index.html')


