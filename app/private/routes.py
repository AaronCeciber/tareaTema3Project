import base64

import password as password
from flask import render_template, redirect, url_for

from . import private
from .models import Cliente

from .forms import FormWTF, Filtrocliente, UsuarioForm, LoginForm
from werkzeug.datastructures import CombinedMultiDict
from flask import request

from ..login.models import Usuario

PEEPER = "ClaveSecretaPeeper"

@private.route("/altacliente/", methods=["GET","POST"])
def altacliente():
    form = FormWTF(CombinedMultiDict((request.files, request.form)))
    # form = FormWTF(request.form)
    if form.validate_on_submit():
        form.nombre.data
        cliente = Cliente()
        cliente.nombre = form.nombre.data
        cliente.dni = form.dni.data
        cliente.apellidos = form.apellidos.data

        encoded_bytes = base64.b64encode(form.imagen.data.read())
        encoded_string = str(encoded_bytes).replace("b'", "").replace("'", "")
        cliente.imagen = encoded_string
        cliente.create()
        return redirect(url_for("private.indexcliente"))

    return render_template("altacliente.html", form = form)


@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    filtro = Filtrocliente(request.form)
    if filtro.validate_on_submit():
        clientes = Cliente.query.filter_by(dni=filtro.dni.data)
    else:
        clientes = Cliente.query.all()
    return render_template("indexcliente.html", clientes = clientes, filtro = filtro)


# @private.route("/hasheadapeeper/", methods=["GET","POST"])
# def hasheadapeeper():
#     error = ""
#     form = UsuarioForm(request.form)
#     if form.validate_on_submit():
#         try:
#             usuario = Usuario()
#             usuario.username = form.username.data
#             password = PEEPER + form.password.data
#             usuario.set_password(password)
#             usuario.nombre = form.nombre.data
#             usuario.apellidos = form.apellidos.data
#             usuario.dni = form.dni.data
#             usuario.create()
#             return redirect(url_for('password.loginhasheadopeeper'))
#         except Exception as e:
#             error = "No se ha podido dar de alta " + e.__str__()
#     return render_template("hasheadapeeper.html", form=form, error=error)


@private.route("/loginhasheadopeeper/", methods=["GET","POST"])
def loginhasheadopeeper():
    error = ""
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = PEEPER + form.password.data
        usuario = Usuario.get_by_username(username)

        if usuario and usuario.check_password(password):
            return redirect(url_for("private.indexcliente"))
        else:
            error = "Usuario y/o contraseña incorrecta"
    return render_template("login.html", form=form, error=error)