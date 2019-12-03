from . import main
from flask import render_template,request,redirect,url_for,abort
from .. import db
from ..request import get_quote
from ..models import User,Blog,Comment
from flask_login import login_required,current_user
from .forms import UpdateProfile,NewBlog,CommentForm
from dominate.tags import comment


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
        user_id = user.id
        title = form.title.data
        topic = form.topic.data
        body = form.body.data

        
        
        new_blog = Blog(title = title,topic = topic,body = body, user_id= user_id)

        new_blog.saves_Blog()
        
        return redirect(url_for('main.new_blog',uname = current_user.username))
    title = "New Blog"
    return render_template('newblog.html',title = title, new_blog_form = form, user = user)

@main.route('/blog', methods = ['GET','POST'])
@login_required
def blog_display():
    blogs = Blog.query.filter_by(user_id=current_user.id)
    return render_template('blog.html', blogs= blogs)
    
@main.route('/blog/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    blog= Blog.query.filter_by(id = id ).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(Blog_id = blog.id, comment = comment, user = current_user.username)
        new_comment.save_comment()
        return redirect(url_for('main.new_blog',id = blog.id))
    title = f'{blog.title} comment'
    return render_template('comment.html',title = title, comment_form = form,blog =blog)

@main.route('/blog/delete/<int:id>')
def delete(id):
    blog = Blog.query.filter_by(id = id).first()
    
    Blog.delete_blog(blog)
    return  redirect(url_for('.blog_display'))

@main.route('/comment/delete/<int:id>')
def delete_comment(id):
    comment = Comment.query.filter_by(id = id).first()
    Comment.delete_comment(comment)    
    return redirect(url_for('.display', id = comment.Blog_id))

@main.route('/blog/comment/display/<int:id>')
def display(id):
    blog = Blog.query.filter_by(id = id).first()
    comment = Comment.query.filter_by(Blog_id = id).all()
    
    return render_template('display.html',comment = comment,blog = blog)

