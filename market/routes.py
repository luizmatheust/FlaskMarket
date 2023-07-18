from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, 
                              email_address=form.email_address.data,
                              password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
        form = LoginForm()
        if form.validate_on_submit():
            user_attempted = User.query.filter(username=form.username.data).first()
            if user_attempted and user_attempted.check_password_correction(attempted_password=form.password.data):
                login_user(user_attempted)
                flash(f'Success! You are logged in as: {user_attempted.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

                 
        return render_template('login.html', form=form)