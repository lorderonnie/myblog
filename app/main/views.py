from . import main
from flask import render_template
from .. import db



@main.route('/')
def index():
    
    '''
    This is the root function of the page
    '''
    title='Ronnieslife'
    return render_template('index.html',title=title)





