from feed import db
from feed.master_tag_type import MasterTagType
from flask.ext.restful import Resource
from flask_restful import fields, marshal
import json

tag_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'thumbnail' : fields.String(attribute='thumbnail')
}
tag_type_fields = {
    'type' : fields.String(attribute='name'),
    'tags' : fields.List(fields.Nested(tag_fields))
}
main_field = {
    'type' : fields.List(fields.Nested(tag_type_fields))
    }

class MasterTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    master_tag_type_id = db.Column(db.Integer,
        db.ForeignKey('master_tag_type.id'))
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
        tag_types  =  MasterTagType.query.all()
        response = []
        for tag_type in tag_types:
             response.append(marshal(tag_type, tag_type_fields))
        return response

