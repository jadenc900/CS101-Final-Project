from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import re
from datetime import datetime

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = str(request.form.get('prefferedemail'))
        school_id = str(request.form.get('schoolId'))
        first_name = str(request.form.get('firstName'))
        last_name = str(request.form.get('lastName'))
        password1 = str(request.form.get('password1'))
        password2 = str(request.form.get('password2'))
        date_of_entry_str = request.form.get('dateOfEntry')
        date_of_entry = datetime.strptime(date_of_entry_str, '%Y-%m-%d')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif len(school_id) > 6:
            flash('Invalid NetID. NetID must be at most 6 characters long.', category='error')
        elif not re.match(r'^\d{3}$', school_id[-3:]):
            flash('Invalid NetID. NetID must end in three integers.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif not (date_of_entry):
            flash('Please enter your date of entry.', category='error')
        else:
            new_user = User(
                email=email,
                password=generate_password_hash(password1, method='sha256'),
                first_name=first_name,
                last_name=last_name,
                date_of_entry=date_of_entry
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)