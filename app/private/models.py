from app import db

class Cliente(db.Model):
    dni = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50))
    imagen = db.Column(db.String())

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            raise