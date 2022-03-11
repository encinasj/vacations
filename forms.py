from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EmpresasForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])