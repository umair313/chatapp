from chatapp import db , login_manager
from flask_login import UserMixin
#this user_loader Decorator is required 
#for user load when sign in
@login_manager.user_loader
def load_user(user_id):
    return  Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(20),nullable=False)
    lastname=db.Column(db.String(20),nullable=False)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(20),nullable=False)


    def __repr__(self):
        return f"Users('{self.firstname}','{self.lastname}','{self.username}','{self.email}')"


