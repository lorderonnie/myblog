from flask_wtf import  FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Email, Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Brief us on who you really are about you.',validators = [Required()])
    submit = SubmitField('Submit')


class NewBlog(FlaskForm):
    title = StringField('Blog name', validators = [Required()])
    topic = StringField('Mention a topic',validators= [Required()])
    body = TextAreaField('Tell us your thoughts on the above topic',validators= [Required()])
    submit = SubmitField('Register')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment down below ',validators=[Required()])
    submit = SubmitField('Submit')       
    
    
    