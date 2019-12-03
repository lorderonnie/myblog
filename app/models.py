from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class Quote():
    '''
    THis is the class used to define the quote objects
    '''
    def __init__(self,id,author,quote):
        self.id = id
        self.author = author
        self.quote = quote
        

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_secure = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
   
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}' 
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    __tablename__ = 'Blog'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    topic = db.Column(db.String(255))
    body = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
   
    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()
    
    
     
    def saves_Blog(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_user_pitch(cls,uname):
        blog = Blog.query.filter_by(user = uname).all()
        
        return blog
    
    @classmethod
    def get_all_blogs(cls):
        blog_list = Blog.query.all()
        return blog_list

class Comment(db.Model):
    __tablename__= 'comment'  
    id = db.Column(db.Integer,primary_key = True)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    comment = db.Column(db.String(255))
    user = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
    Blog_id = db.Column(db.Integer)
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get_blog_comment(cls,id):
        comment = Comment.query.filter_by(Blog_id = id)

        return comment  