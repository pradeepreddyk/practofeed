from feed import db

class MasterTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    master_type = db.Column(db.String(80))
    thumbnail = db.Column(db.String(256))
    parent_id = db.Column(db.Integer, db.ForeignKey('master_tag.id'))                  
    parent = db.relationship('MasterTag',                                               
       backref=db.backref('children', lazy='dynamic'),
       remote_side=id)

    def __init__(self, name, master_type, thumbnail, parent=None):
        self.name = name
        self.parent = parent
        self.master_type = master_type
        self.thumbnail = thumbnail

    def __repr__(self):
        return '<MasterTag %r>' % self.name

