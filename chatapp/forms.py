from flask_wtf import FlaskForm
from wtforms import PasswordField ,StringField, BooleanField, SubmitField
from wtforms.validators import Email, EqualTo, ValidationError , length , DataRequired
from chatapp.models import Users


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name',validators=[DataRequired()])
    lastname = StringField('Last Name',validators=[DataRequired()])
    username = StringField('User Name',validators=[DataRequired(),length(min=2,max=20)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    confirm_password= PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self,username):
        user = Users.query.filter_by(username= username.data).first()
        if user:
            raise ValidationError(f'Username {self.username} already exit.Please try different')

    def validate_email(self,email):
        user = Users.query.filter_by(email= email.data).first()
        if user:
            raise ValidationError(f'Email {self.email} already exit.Please try different')



class LoginForm(FlaskForm):
    
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")