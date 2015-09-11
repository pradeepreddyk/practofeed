from feed import db
from feed.user import User
from feed.master_publisher import MasterPublisher

class PublisherFollow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    master_publisher_id = db.Column(db.Integer,
        db.ForeignKey('master_publisher.id'))
    master_publisher = db.relationship('MasterPublisher')

    def __init__(self, user, master_publisher):
        self.user = user
        self.master_publisher = master_publisher

