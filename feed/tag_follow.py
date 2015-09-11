from feed import db
from feed.user import User
from feed.master_tag import MasterTag

class TagFollow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    master_tag_id = db.Column(db.Integer, db.ForeignKey('master_tag.id'))
    master_tag = db.relationship('MasterTag')

    def __init__(self, user, master_tag):
        self.user = user
        self.master_tag = master_tag

