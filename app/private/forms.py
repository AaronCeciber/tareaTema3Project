from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms.validators import DataRequired, Length, ValidationError

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


class UsuarioForm(FlaskForm):

    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=15, message="El nombre de usuario no puede ser superior a 20 caracteres")
    ])

    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña debe tener al menos 8 caracteres")
    ])

    nombre = StringField(label="Nombre", validators=[
        DataRequired(message="El nombre es obligatorio"),
        Length(max=20, message="El nombre no puede ser superior a 20 caracteres")
    ])

    apellidos = StringField(label="Apellidos", validators=[
        DataRequired(message="Los apellidos son obligatorio"),
        Length(max=50, message="Los apellidos no pueden superar los 50 caracteres")
    ])

    # submit = SubmitField(label="Dar de alta")

    def validate_password(form,field):
        if str(field.data).isdigit():
            raise ValidationError("La contraseña no pueden ser solo dígitos")
        if field.data != form.passwordRepeat.data:
            raise ValidationError("No coinciden las contraseñas")

    def validate_passwordRepeat(form, field):
        if field.data != form.password.data:
            raise ValidationError("No coinciden las contraseñas")


class LoginForm(FlaskForm):
    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=15, message="El nombre de usuario no puede ser superior a 15 caracteres")
    ])

    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])