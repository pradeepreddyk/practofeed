from feed import db

class MasterTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('master_tag.id'))                  
    parent = db.relationship('MasterTag',                                               
       backref=db.backref('children', lazy='dynamic'),
       remote_side=id)

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def __repr__(self):
        return '<User %r>' % self.username

