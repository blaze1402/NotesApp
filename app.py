from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Note(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(1500), nullable=False)
    time=db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"{self.Sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        time=datetime.now().strftime('%H:%M %d/%m/%Y')
        note=Note(title=title, desc=desc, time=time)
        db.session.add(note)
        db.session.commit()
        
    allNotes=Note.query.all()
    return render_template("index.html", allNotes=allNotes)

@app.route('/edit/<int:sno>', methods=['GET', 'POST'])
def edit(sno):
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        note=Note.query.filter_by(sno=sno).first()
        note.title=title
        note.desc=desc
        note.time=datetime.now().strftime('%H:%M %d/%m/%Y')
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index_page'))

    note=Note.query.filter_by(sno=sno).first()
    return render_template("edit.html", note=note)

@app.route('/delete/<int:sno>')
def delete(sno):
    note=Note.query.filter_by(sno=sno).first()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index_page'))

if __name__ == "__main__":
    app.run(debug=True)