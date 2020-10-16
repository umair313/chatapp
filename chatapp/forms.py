from flask_wtf import FlaskForm
from wtforms import PasswordField ,StringField, BooleanField, SubmitField
from wtforms.validators import Email, EqualTo, ValidationError , length , DataRequired



class RegistrationForm(FlaskForm):
    firstname = StringField('First Name',validators=[DataRequired()])
    lastname = StringField('Last Name',validators=[DataRequired()])
    username = StringField('User Name',validators=[DataRequired(),length(min=2,max=20)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    confirm_password= PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")