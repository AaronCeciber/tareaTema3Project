from flask import render_template, redirect, url_for
from .forms import LoginForm, UsuarioForm
from .models import Usuario
from flask import request
from . import login
from flask_login import current_user, logout_user, login_user

from .. import app

PEEPER = "ClaveSecretaPeeper"

@app.login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(user_id)

@login.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('public.index'))


@login.route("/altausuario/", methods=["GET","POST"])
def altausuario():
    error = ""
    form = UsuarioForm(request.form)
    if form.validate_on_submit():
        try:
            usuario = Usuario()
            usuario.username = form.username.data
            password = PEEPER + form.password.data
            usuario.set_password(password)
            usuario.nombre = form.nombre.data
            usuario.apellidos = form.apellidos.data
            if request.form.get('is_admin'):
                usuario.is_admin = True
            usuario.create()
            return redirect(url_for('login.login'))
        except Exception as e:
            error = "No se ha podido dar de alta " + e.__str__()
    return render_template("altausuario.html", form=form, error=error)


@login.route("/login/", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    error = ""
    formlogin = LoginForm(request.form)
    if formlogin.validate_on_submit():
        username = formlogin.username.data
        password = PEEPER + formlogin.password.data
        usuario = Usuario.get_by_username(username)

        if usuario and usuario.check_password(password):
            login_user(usuario)
            return redirect(url_for("private.indexcliente"))
        else:
            error = "Usuario y/o contraseña incorrecta"
    return render_template("login.html", formlogin=formlogin, error=error)



