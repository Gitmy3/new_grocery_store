from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username = username).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login Succesful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid Username or Password', 'error')
    return render_template('login.html.jinja2')

# For Log-out
@auth_bp.route('/logout')
@login_required

def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

