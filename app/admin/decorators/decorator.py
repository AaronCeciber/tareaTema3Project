from functools import wraps

from flask import render_template
from flask_login import current_user
from werkzeug.exceptions import abort

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(current_user, 'is_admin', False)
        if not is_admin:
            # abort(401)
        # return f(*args, **kws)
            return render_template("accesodenegado.html")
    return decorated_function