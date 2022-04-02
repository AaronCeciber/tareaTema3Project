from flask import render_template
from flask_login import login_required


from app.admin import admin
from app.admin.decorators.decorator import admin_required
from app.login.models import Usuario


@admin.route("/indexusuario/", methods=["GET","POST"])
@login_required
@admin_required
def indexusuario():
    usuarios = Usuario.query.all()
    return render_template("indexusuario.html", usuarios = usuarios)




