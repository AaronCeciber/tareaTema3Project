from flask import render_template, redirect, url_for
from .forms import LoginForm, UsuarioForm
from .models import Usuario
from flask import request
from . import login

PEEPER = "ClaveSecretaPeeper"

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
            usuario.create()
            return redirect(url_for('login.login'))
        except Exception as e:
            error = "No se ha podido dar de alta " + e.__str__()
    return render_template("altausuario.html", form=form, error=error)


@login.route("/login/", methods=["GET", "POST"])
def login():
    error = ""
    formlogin = LoginForm(request.form)
    if formlogin.validate_on_submit():
        username = formlogin.username.data
        password = PEEPER + formlogin.password.data
        usuario = Usuario.get_by_username(username)

        if usuario and usuario.check_password(password):
            return redirect(url_for("private.indexcliente"))
        else:
            error = "Usuario y/o contraseña incorrecta"
    return render_template("login.html", formlogin=formlogin, error=error)


