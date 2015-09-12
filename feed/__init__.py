from flask import Flask, request, session, g, redirect, url_for, \
         abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api


# configuration
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/feed'
DEBUG = True

# initialize flask app and set config
app = Flask(__name__)
app.config.from_object(__name__)

# initialize alchemy DB object
db = SQLAlchemy(app)
from feed.user import User, UserApi
from feed.source import Source
from feed.article import Article, ArticleApi
from feed.master_tag_type import MasterTagType
from feed.master_tag import MasterTag, TagApi
from feed.article_tag import ArticleTag
from feed.tag_follow import TagFollow
from feed.user_follow import UserFollow
from feed.master_publisher import MasterPublisher
from feed.publisher_follow import PublisherFollow
from feed.user_article_action import UserArticleAction

# Api
api = Api(app)
api.add_resource(ArticleApi, '/article')
api.add_resource(UserApi, '/user')
api.add_resource(TagApi, '/tag')

# For now define routes here
@app.route("/")
def hello():
  admin = User.query.filter_by(role='admin').first()
  if not admin:
    return "No admin"
  return "admin email is " + admin.email

@app.cli.command('initdb')
def initdb_command():
    """Initialize the database."""
    print 'Init the db'
    db.drop_all()
    db.create_all()
    admin = User('admin', 'admin@example.com','admin')
    db.session.add(admin)
    master_tag_type1 = MasterTagType('Everyday Health Tip',
        'http://www.exisoftware.com/thumbnail_generator/'+
        'sample-galleries/basic-web-photo-gallery/thumbs/tn_4310.jpg')
    master_tag_type2 = MasterTagType('Health Conditions',
        'http://www.exisoftware.com/thumbnail_generator/'+
        'sample-galleries/basic-web-photo-gallery/thumbs/tn_5183.jpg')
    master_tag_type3 = MasterTagType('Health News',
        'http://www.exisoftware.com/thumbnail_generator/'+
        'sample-galleries/basic-web-photo-gallery/thumbs/tn_4311.jpg')
    db.session.add(master_tag_type1)
    db.session.add(master_tag_type2)
    db.session.add(master_tag_type3)

    master_tag1 = MasterTag('General Health',
        master_tag_type1, 
        'http://www.exisoftware.com/thumbnail_generator/'+                       
        'sample-galleries/basic-web-photo-gallery/thumbs/tn_5184.jpg')
    master_tag2 = MasterTag('New Born',
        master_tag_type1, 
        'http://www.exisoftware.com/thumbnail_generator/'+                       
        'sample-galleries/basic-web-photo-gallery/thumbs/tn_5184.jpg')
    master_tag3 = MasterTag('Hair',
        master_tag_type1, 
        'http://www.exisoftware.com/thumbnail_generator/'+                       
        'sample-galleries/basic-web-photo-gallery/thumbs/tn_5185.jpg')
    master_tag4 = MasterTag('Fitness',
        master_tag_type1, 
        'http://www.exisoftware.com/thumbnail_generator/'+                       
        'sample-galleries/basic-web-photo-gallery/thumbs/tn_5186.jpg')
    master_tag21 = MasterTag('Hair Fall',
        master_tag_type2, 
        'http://www.exisoftware.com/thumbnail_generator/'+                       
        'sample-galleries/basic-web-photo-gallery/thumbs/tn_5187.jpg')
    db.session.add(master_tag1)
    db.session.add(master_tag2)
    db.session.add(master_tag3)
    db.session.add(master_tag4)
    db.session.add(master_tag21)
    db.session.commit()

