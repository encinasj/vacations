from .app import db


class MicroBusiness(db.Model):
    __tablename__ = 'microbusiness'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    employees = db.relationship('Employee', backref=db.backref('microbusiness', lazy='joined'), lazy='select' )

    def __str__(self):
        return (
            f'id: {self.id}'
            f'name: {self.name}'
        )

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80))
    admission_date = db.Column(db.Date, default=False)
    salary_per_day = db.Column(db.Float, default=False)
    percent = db.Column(db.Integer, default=False)
    microbusiness_id = db.Column(db.Integer, db.ForeignKey('microbusiness.id'), nullable=False)


    def __str__(self):
        return(
            f'id: {self.id}'
            f'full_name: {self.full_name}'
        )
