
from flask import render_template,redirect , url_for, request , flash
from chatapp.forms import RegistrationForm, LoginForm
from chatapp import app



@app.route('/')
def home():
    return render_template('home.html', title= 'ShareNow')


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Sucess!", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login' ,methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('You are Loged in','success')
        return redirect(url_for('home'))
    #else:
        #flash('Please Check your Email Password!','danger')
    return render_template('login.html', title = 'Login',form=form)