from .app import db


class Empresas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __str__(self):
        return (
            f'id: {self.id}, '
            f'name: {self.name}'
        )
