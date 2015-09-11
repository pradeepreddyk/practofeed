from feed import db

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    url = db.Column(db.String(256))

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return '<Source %r>' % self.name

