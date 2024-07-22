from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .views import views


auth = Blueprint('auth',__name__)

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if user:= User.query.filter_by(email=email).first():
            flash('Email already exists',category='error')
        elif len(email) < 4:
            flash('Email must be at least 4 characters',category='error')
        elif len(name) < 2:
            flash('Name must be at least 2 characters',category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters',category='error')
        elif password1 != password2:
            flash('Passwords do not match',category='error')
        else:
            hashed_password = generate_password_hash(password1,method='pbkdf2:sha256')
            new_user = User(email=email,name=name,password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash('Account created successfully',category='success')
            
            return redirect(url_for('views.home'))
        
    return render_template('signup.html')


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully',category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again',category='error')   
        else:
            flash('Email does not exist', category='error')
            
    return render_template('login.html',user=current_user)



@auth.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))
