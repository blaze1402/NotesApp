from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField

#Adding a registration form in the register page
class RegisterForm(FlaskForm):
    
    #input types used in register form
    username=StringField()
    email=EmailField()
    password=PasswordField()
    confirmPassword=PasswordField()
    submit=SubmitField(label="Sign Up")

#Adding a login form in the login page
class LoginForm(FlaskForm):

    #input types used in login form
    email=EmailField()
    password=PasswordField()
    submit=SubmitField(label="Log In")