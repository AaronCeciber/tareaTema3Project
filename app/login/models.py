import os

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, app


class Usuario(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.nombre + self.apellidos

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            app.logger.info("Se ha creado el usuario " + self.__str__())
        except:
            app.logger.exception("Error al insertar el usuario " + self.__str__())
            raise

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def get_by_username(username):
        return Usuario.query.filter_by(username=username).first()


    def set_password(self, password):
        # self.password = generate_password_hash(password, method='pbkdf2:sha512')
        method = "pbkdf2:sha256:260000"
        # method = "plain"
        # method = "pbkdf2:sha512:10000000"
        self.password = generate_password_hash(password,method=method) #Por defecto sha256
        # self.password = password.split("$", 1)[1]


    def check_password(self, password):
        # passHash = 'pbkdf2:sha256:260000$' + self.password
        return check_password_hash(self.password, password)