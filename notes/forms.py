from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired

# Adding a registration form in the register page
class RegisterForm(FlaskForm):

    # input types and validators used in registeration form
    username = StringField(validators=[Length(min=5, max=30), DataRequired()])
    email = StringField(validators=[Email(), DataRequired()])
    password = PasswordField(validators=[Length(min=8), DataRequired()])
    confirmPassword = PasswordField(validators=[EqualTo("password"), DataRequired()])
    submit = SubmitField(label="Sign Up")


# Adding a login form in the login page
class LoginForm(FlaskForm):

    # input types and validators used in login form
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField(label="Log In")
