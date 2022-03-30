from .app import db

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    admission_date = db.Column(db.Date, default=False)
    salary_per_day = db.Column(db.Float, default=False)
    percent = db.Column(db.Integer, default=False)
    namecompany = db.Column(db.String(80), unique=True, nullable=False)




