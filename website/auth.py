from flask import Blueprint, render_template, request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET' , 'POST'])

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password =  request.form.get('password')
        user = User.query.filter_by(email=email).first()
      
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return  render_template("index.html", user=current_user)

@auth.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/index', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email_signup = request.form.get('emailSignUp')
        password_signup = request.form.get('passwordSignUp')
        confirm_password = request.form.get('confirmPassword')

        user = User.query.filter_by(email=email_signup).first()    
        if user:
            flash('Email Already Exist', category='error')
        elif len(email_signup) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif password_signup != confirm_password:
            flash('Password dont match .', category='error') 
        else:
            new_user = User(email=email_signup, password=generate_password_hash(password_signup, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created ! ' ,category='success')
        return render_template("index.html", user=current_user)
    
