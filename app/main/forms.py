from flask_wtf import  FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('BRief us on who you really are about you.',validators = [Required()])
    submit = SubmitField('Submit')


