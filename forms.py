from ntpath import join
from select import select
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField,DateField,FloatField,IntegerField
from datetime import date
from wtforms.validators import DataRequired, ValidationError, Length


from .models import Employee


class EmployeesForm(FlaskForm):
    full_name = StringField('full_name', validators=[DataRequired(), Length(min=10, max=60, message='Nombre de 10 a 60 Caracteres')])
    admission_date = DateField('admission_date', default=date.today, validators=[DataRequired()])
    salary_per_day = FloatField('salary_per_day', validators=[DataRequired()])
    percent = IntegerField('percent', validators=[DataRequired()])
    namecompany = StringField('namecompany', validators=[DataRequired()])


    def validate_name(self, full_name):
        Employename = Employee.query.filter_by(full_name=full_name.data).first()
        if Employename is not None:
          raise ValidationError('Colaborador ya existente.')

    