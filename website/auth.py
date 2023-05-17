from flask import Blueprint, render_template, request, flash
from flask_login import current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", user=current_user, username="Sylwia")

@auth.route('/logout')
def logout():
    return 0

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password1')
        password2 = request.form.get('password2')

        if password != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password) < 5:
            flash('Password must be at least 5 characters', category='error')
        else:
            # add user to database
            flash('Account created', category='success')

    return render_template("sign_up.html", user=current_user)