
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
# app configuration
app.config['SECRET_KEY'] = '3652552d15c9b466d7c09f69044c8a94'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse.db'
hash_pass = Bcrypt(app)
## creating Database Object
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view='login'

from chatapp import views
