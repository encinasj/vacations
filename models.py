from .app import db


class Empresas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    employes = db.relationship('Employes', backref='Empresas')

    def __str__(self):
        return (
            f'id: {self.id}, '
            f'name: {self.name}'
        )

class Employes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column()
    admission_date = db.Column()
    salary_per_day = db.Column()
    percent = db.Column()
    empresas_id = db.Column(db.Integer, db.ForeignKey('empresas.id'))
