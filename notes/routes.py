from flask import redirect, render_template, request, url_for
from datetime import datetime
from notes.forms import LoginForm, RegisterForm
from notes import app, db
from notes.models import Note

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
@app.route("/register")
def register_page():
    form = RegisterForm()
    if form.validate_on_submit:
        form.username

    return render_template("register.html", form=form)


# login page of the website
@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit:
        pass

    return render_template("login.html", form=form)


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
