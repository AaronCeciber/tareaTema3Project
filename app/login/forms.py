from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms.validators import DataRequired, Length, ValidationError

class UsuarioForm(FlaskForm):

    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=15, message="El nombre de usuario no puede ser superior a 20 caracteres")
    ])

    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña debe tener al menos 8 caracteres")
    ])

    passwordRepeat = PasswordField(label="Repetir contraseña", validators=[
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

    submit = SubmitField(label="Dar de alta")

    def validate_password(form,field):

        caracteresEspeciales = ['#','$','%','&']

        if not any(char.isdigit() for char in field.data):
            raise ValidationError("La contraseña debe contener al menos 1 dígito")
        if not any(char.isupper() for char in field.data):
            raise ValidationError("La contraseña debe contener al menos 1 letra mayúscula")
        if not any(char in field.data for char in caracteresEspeciales):
            raise ValidationError("La contraseña debe contener al menos 1 caracter especial '# $ % &'")

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