from notes import db


class Note(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(1500), nullable=False)
    time = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"{self.Sno} - {self.title}"
