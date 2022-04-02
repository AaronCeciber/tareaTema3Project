from app import db, app


class Cliente(db.Model):
    dni = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50))
    imagen = db.Column(db.String())

    def __str__(self):
        return "dni: " + self.dni + " nombre: " + self.nombre + " apellidos: " + self.apellidos

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            app.logger.info("Se ha creado el cliente " + self.__str__())
        except:
            app.logger.exception("Error al insertar el cliente " + self.__str__())
            raise