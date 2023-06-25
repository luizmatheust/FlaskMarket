from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Username:')
    email_address = StringField(label='Email:')
    password = PasswordField(label='Password:')
    password_confirmation = PasswordField(label='Password Confirmation:')
    submit = SubmitField(label='Create Account')
