from flask import render_template
from . import public
# from flask import request
# from ..login.forms import LoginForm


@public.route('/')
def index():  # put application's code here
    return render_template('index.html')


