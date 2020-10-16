
from flask import Flask

app = Flask(__name__)
# app configuration
app.config['SECRET_KEY'] = '3652552d15c9b466d7c09f69044c8a94'
from chatapp import views
