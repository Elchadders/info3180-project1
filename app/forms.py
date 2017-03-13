from flask_wtf import FlaskForm
from wtforms import StringField, TextField, FileField, file_required, RadioField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = RadioField('Gender', choices=[('male'),('female')])
    biography = TextField('biography', validators=[InputRequired()])
    image = FileField('Image', validators=[file_required()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    
