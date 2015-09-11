from feed import db
from feed.article import Article
from feed.user import User
from datetime import datetime

class UserArticleAction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    action_type = db.Column(db.String(20))
    created_at = db.Column(db.DateTime)
    comment = db.Column(db.String(256))

    def __init__(self, article, user, action_type, comment, created_at=None):
        self.article = article
        self.user = user
        self.action_type = action_type
        self.comment = comment
        if created_at is None:                                                   
            created_at = datetime.utcnow()                                       
        self.created_at = created_at
