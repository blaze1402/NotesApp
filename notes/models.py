from notes import db, login_manager, bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=31), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    notes = db.relationship("Note", backref="saved_notes", lazy=True)

    def __repr__(self) -> str:
        return f"{self.username}"
    
    #this @property decorator is used to get or set the password attribute by making it easily accessible
    @property
    def password(self):
        return self.password

    #here @password.setter is used by @property decorator to easily set the password attribute
    @password.setter
    def password(self, plain_text_password):
        self.password_hash=bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    #this is used to check the attempted password typed during login attempt
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)



class Note(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(1500), nullable=False)
    time = db.Column(db.String, nullable=False)
    saved = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self) -> str:
        return f"{self.Sno} - {self.title}"
