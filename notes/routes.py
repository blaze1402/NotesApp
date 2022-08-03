from flask_login import login_user, logout_user
from flask import flash, redirect, render_template, request, url_for
from datetime import datetime
from notes.forms import LoginForm, RegisterForm
from notes import app, db
from notes.models import Note, User

# homepage of the website
@app.route("/", methods=["GET", "POST"])
def index_page():

    # Whenever a post request is received then this if block will execute and save a note to the database
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        time = datetime.now().strftime("%H:%M %d/%m/%Y")
        note = Note(title=title, desc=desc, time=time)
        db.session.add(note)
        db.session.commit()

    # otherwise the saved notes will be shown to the users
    allNotes = Note.query.all()
    return render_template("index.html", allNotes=allNotes)


# registration page of the website
@app.route("/register", methods=["GET", "POST"])
def register_page():

    #created a RegisterForm object as form
    form = RegisterForm()

    #this condition is used to create a user when the validation of the form is completed this is done on the submit button of the form
    if form.validate_on_submit():
        create_user=User(username=form.username.data,
                         email=form.email.data,
                         password_hash=form.password.data)
        db.session.add(create_user)
        db.session.commit()
        login_user(create_user)
        flash(f'Account created successfully! You are now logged in as {create_user.username}!', category='success')
        return redirect(url_for('index_page'))

    #this condition displays the errors done while submitting the form
    if form.errors!={}:
        for errors in form.errors.values():
            flash(f"There was an error with creating a user: {errors}", category='danger')
    return render_template("register.html", form=form)


# login page of the website
@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user=User.query.filter_by(username=form.username.data).first()
        attempted_password=User.query.filter_by(password_hash=form.password.data).first()
        if attempted_user and attempted_password:
            login_user(attempted_user)
            flash(f'You have been successfully logged in as {attempted_user.username}!', category='success')
            return redirect(url_for('index_page'))
        else:
            flash('Username and password do not match! Please try again.', category='danger')

    return render_template("login.html", form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'You have been logged out!', category='info')
    return redirect(url_for('index_page'))


@app.route("/edit/<int:sno>", methods=["GET", "POST"])
def edit(sno):
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        note = Note.query.filter_by(sno=sno).first()
        note.title = title
        note.desc = desc
        note.time = datetime.now().strftime("%H:%M %d/%m/%Y")
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("index_page"))

    note = Note.query.filter_by(sno=sno).first()
    return render_template("edit.html", note=note)


@app.route("/delete/<int:sno>")
def delete(sno):
    note = Note.query.filter_by(sno=sno).first()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("index_page"))
