
from flask import render_template,redirect , url_for, request , flash
from chatapp.forms import RegistrationForm, LoginForm
from chatapp.models import Users
from flask_login import login_user, current_user , logout_user ,login_required
from chatapp import app, db , hash_pass



@app.route('/')
def home():
    #if user already login then dont show home page
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    return render_template('home.html', title= 'ShareNow')


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # add user into database
        add_user(form)
        # display successfull registration 
        # and form information to user
        flash(f"Account Created wil the following information.<br>"
                f"Username: {form.username.data} <br>"
                f"Email: {form.email.data} <br>"
                f"First Name: {form.firstname.data} <br>"
                f"Last Name: {form.lastname.data} <br>",
         'success')
         #now load login form if register 
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login' ,methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash('Dear user you already login','success')
        return redirect(url_for('profile'))
    form=LoginForm()
    if form.validate_on_submit():
        #check if email is exit in database 
        #check password is correct
        user = Users.query.filter_by(email=form.email.data).first()
        if user and hash_pass.check_password_hash(user.password, form.password.data):
            #if data is correct then loginuser
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            flash('You are Loged in','success')
            return redirect(next_page) if next_page else redirect(url_for('profile'))
    #else:
        #flash('Please Check your Email Password!','danger')
    return render_template('login.html', title = 'Login',form=form)

#when user login then redirect to profile page
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title = current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logout I hope we see you soon!','success')
    return redirect(url_for('home'))




def add_user(form):
    newuser = Users(firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=hashed_password(form),
                    username=form.username.data)
    db.session.add(newuser)
    db.session.commit()

def hashed_password(form):
    return hash_pass.generate_password_hash(form.password.data).decode('utf-8')
