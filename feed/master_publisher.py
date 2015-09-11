from feed import db

class MasterPublisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    publisher_type = db.Column(db.String(20))

    def __init__(self, name, publisher_type):
        self.name = name
        self.publisher_type = publisher_type

    def __repr__(self):
        return '<User %r>' % self.name

