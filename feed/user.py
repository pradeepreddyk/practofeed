from feed import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    photo_url = db.Column(db.String(256), unique=True)
    role = db.Column(db.String(256), unique=True)

    def __init__(self, username, email, role = '', photo_url=''):
        self.username = username
        self.email = email
        self.role = role
        self.photo_url = photo_url

    def __repr__(self):
        return '<User %r>' % self.username

