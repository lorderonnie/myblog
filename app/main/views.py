from . import main
from flask import render_template,request,redirect,url_for,abort
from .. import db
from ..request import get_quote
from ..models import User,Blog
from flask_login import login_required,current_user
from .forms import UpdateProfile,NewBlog


@main.route('/')
def index():
    
    '''
    This is the root function of the page
    '''
    title='Ronnieslife'
    quote_name= get_quote()
    return render_template('index.html',title=title,quote_name = quote_name)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/blog/new/<uname>' ,methods=["GET",'POST'])
def new_blog(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = NewBlog()
    if form.validate_on_submit():
        title = form.title.data
        topic = form.topic.data
        body = form.body.data

        
        
        new_blog = Blog(title = title,topic = topic,body = body)

        new_blog.saves_Blog()
        
        return redirect(url_for('main.new_blog',uname = current_user.username))
    title = "New Blog"
    return render_template('newblog.html',title = title, new_blog_form = form, user = user)







