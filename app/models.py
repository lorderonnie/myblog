from . import db 

class Quote():
    '''
    THis is the class used to define the quote objects
    '''
    def __init__(self,id,author,quote):
        self.id = id
        self.author = author
        self.quote = quote
        
    
        



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'