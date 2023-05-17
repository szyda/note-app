from flask import Blueprint
from flask import render_template
from flask_login import current_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", user=current_user, username="Sylwia")

@auth.route('/logout')
def logout():
    return 0

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html", user=current_user)