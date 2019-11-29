from . import main
from flask import render_template,request,redirect,url_for
from .. import db
from ..request import get_quote
from ..models import User
from flask_login import login_required



@main.route('/')
def index():
    
    '''
    This is the root function of the page
    '''
    title='Ronnieslife'
    quote_name= get_quote()
    return render_template('index.html',title=title,quote_name = quote_name)





