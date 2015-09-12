from feed import db
from feed.master_tag_type import MasterTagType
from flask.ext.restful import Resource

class MasterTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    master_tag_type_id = db.Column(db.Integer, db.ForeignKey('master_tag_type.id'))
    master_tag_type = db.relationship('MasterTagType',
       backref=db.backref('tags', lazy='dynamic'))
    thumbnail = db.Column(db.String(256))
    parent_id = db.Column(db.Integer, db.ForeignKey('master_tag.id'))                  
    parent = db.relationship('MasterTag',
       backref=db.backref('children', lazy='dynamic'),
       remote_side=id)

    def __init__(self, name, master_tag_type, thumbnail, parent=None):
        self.name = name
        self.parent = parent
        self.master_tag_type = master_tag_type
        self.thumbnail = thumbnail

    def __repr__(self):
        return '<MasterTag %r>' % self.name

class TagApi(Resource):                                                      
    def get(self):
        return {'class': 'article', 'first': 'john', 'last': 'doe'}

