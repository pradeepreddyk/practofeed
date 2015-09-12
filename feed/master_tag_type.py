from feed import db
from flask.ext.restful import Resource

class MasterTagType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    thumbnail = db.Column(db.String(256))

    def __init__(self, name, thumbnail):
        self.name = name
        self.thumbnail = thumbnail

    def __repr__(self):
        return '<MasterTagType %r>' % self.name

