from feed import db
from feed.source import Source
from feed.user import User
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('articles', lazy='dynamic'))
    is_primary_author = db.Column(db.Boolean)

    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    source = db.relationship('Source',
        backref=db.backref('articles', lazy='dynamic'))

    def __init__(self, title, content, source, author, is_primary_author= False,
        created_at=None ):
        self.title = title
        self.content = content
        if created_at is None:
            created_at = datetime.utcnow()
        self.created_at = created_at
        self.source = source
        self.author = author
        self.is_primary_author = is_primary_author

    def __repr__(self):
        return '<Article %r>' % self.title

