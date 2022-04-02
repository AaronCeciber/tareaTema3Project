import base64

from flask import render_template, redirect, url_for
from flask_login import login_required

from . import private
from .models import Cliente

from .forms import FormWTF, Filtrocliente
from werkzeug.datastructures import CombinedMultiDict
from flask import request




@private.route("/altacliente/", methods=["GET","POST"])
def altacliente():
    form = FormWTF(CombinedMultiDict((request.files, request.form)))
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
@login_required
def indexcliente():
    filtro = Filtrocliente(request.form)
    if filtro.validate_on_submit():
        clientes = Cliente.query.filter_by(dni=filtro.dni.data)
    else:
        clientes = Cliente.query.all()
    return render_template("indexcliente.html", clientes = clientes, filtro = filtro)




