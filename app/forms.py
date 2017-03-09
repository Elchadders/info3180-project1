from flask.ext.wtf import Form
from wtforms.fields import TextField, RadioField 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import Required

class UserForm(Form):
	first_name = TextField("first_name", validators=[Required()])
	last_name = TextField("last_name", validators=[Required()])
	gender = RadioField("gender", choices=[
		('male', 'Male'), 
		('female', 'Female')
	])
	age = TextField("age", validators=[Required()])
	image = FileField("image", validators=[
		FileRequired(),
		FileAllowed(['jpg', 'png'], "Images only!")
	])