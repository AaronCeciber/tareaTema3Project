from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms.validators import DataRequired, Length

class FormWTF(FlaskForm):

    dni = StringField(label="Dni", validators=[
        DataRequired(message="El campo DNI es obligatorio"),
        Length(max=10, message="El campo DNI debe ser de 10 caracteres")
    ])

    nombre = StringField(label="Nombre",validators=[
        DataRequired(message="El campo Nombre es obligatorio"),
        Length(max=20,message="El campo Nombre tiene como máximo 20 caracteres")
    ])

    apellidos = StringField(label="Apellidos", validators=[
        DataRequired(message="El campo Apellidos es obligatorio"),
        Length(max=50, message="El campo Apellidos tiene como máximo 50 caracteres")
    ])

    edad = IntegerField(label="Edad")

    imagen = FileField(label="Imagen", validators=[
        FileRequired(message="El campo imagen es obligatorio"),
        FileAllowed(['jpg','png'], message="Solo jpg y png")
    ])

    submit = SubmitField(label="Enviar")


class Filtrocliente(FlaskForm):
    dni = StringField(label="Dni", validators=[
        DataRequired(message="El campo DNI es obligatorio"),
        Length(max=10, message="El campo DNI debe ser de 10 caracteres")])
    submit = SubmitField(label="Filtrar")