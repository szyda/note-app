from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password.', category='error')
        else:
            flash('Account doens\'t exists', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email)
        if user:
            flash('Account already exists', category='error')
            return redirect(url_for('auth.login'))
        if password != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password) < 5:
            flash('Password must be at least 5 characters', category='error')
        else:
            add_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(add_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)