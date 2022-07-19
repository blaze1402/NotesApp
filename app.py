from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    Sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(1000), nullable=False)
    time=db.Column(db.DateTime,default=datetime.now())

@app.route('/')
@app.route('/home')
def index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)