from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class MovementsForm(FlaskForm):
    Date = DateField('Fecha', validators=[DataRequired(message="La fecha es requerida")])
    Description = StringField('Descripción', validators=[DataRequired(message="Debes ingresar una descripción"), Length(min=4, message="La descripción debe tener más de 4 caracteres")])
    Value = FloatField('Valor', validators=[DataRequired(message="Debes ingresar valores diferentes a 0")])
    button = SubmitField('Crear')

    def validate_Date(form, field):
        if field.data > date.today():
            raise ValidationError("Fecha inválida: La fecha introducida es a futuro")
            
