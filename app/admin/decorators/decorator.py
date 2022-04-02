from functools import wraps

from flask import render_template
from flask_login import current_user
from werkzeug.exceptions import abort

from app import app


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(current_user, 'is_admin', False)
        if not is_admin:
            app.logger.warning("Advertencia de acceso no autorizado")
            return render_template("accesodenegado.html")
        return f(*args, **kws)
    return decorated_function