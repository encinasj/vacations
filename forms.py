from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, length

from .models import Empresas

class EmpresasForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message='nombre repetido'), length(min=2, max=20)])

    def validate_name(self, name):
        Companyname = Empresas.query.filter_by(name=name.data).first()
        if Companyname is not None:
          raise ValidationError('Ese micronegocio ya existe.')
