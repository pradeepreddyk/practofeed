from feed import db
from feed.article import Article
from feed.master_tag import MasterTag

class ArticleTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_tag_name = db.Column(db.String(120))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    article = db.relationship('Article',
        backref=db.backref('tags', lazy='dynamic'))

    master_tag_id = db.Column(db.Integer, db.ForeignKey('master_tag.id'))
    master_tag = db.relationship('MasterTag',
        backref=db.backref('article_tags', lazy='dynamic'))

    def __init__(self, article_tag_name, article, master_tag):
        self.article_tag_name = article_tag_name
        self.article = article
        self.master_tag = master_tag

    def __repr__(self):
        return '<Article %r>' % self.article_tag_name 

