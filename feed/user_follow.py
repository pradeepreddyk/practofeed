from feed import db
from feed.user import User

class UserFollow(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        primary_key=True)

    follower_id = db.Column(db.Integer,
        db.ForeignKey('user.id', name='follower_id'),
        primary_key=True)

