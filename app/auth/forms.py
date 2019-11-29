from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your new username',validators = [Required()])
    password = PasswordField('Password *use a mix of letters and symbols*, eg:rrr$%#dffG',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must be matching')])
    password_confirm = PasswordField('Validate Password',validators = [Required()])
    submit = SubmitField('Sign Up!!')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('SORRY PAL!!! An account with that email has been inputed')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is in use')

class LoginForm(FlaskForm):
    email = StringField('Enter your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password please...',validators =[Required()])
    remember = BooleanField('You might wanna remember me')
    submit = SubmitField('Sign In')





