from flask import Flask, request, session, g, redirect, url_for, \
         abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy


# configuration
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/feed'
DEBUG = True

# initialize flask app and set config
app = Flask(__name__)
app.config.from_object(__name__)

# initialize alchemy DB object
db = SQLAlchemy(app)
from feed.user import User
from feed.source import Source
from feed.article import Article
from feed.master_tag import MasterTag
from feed.master_publisher import MasterPublisher
from feed.article_tag import ArticleTag
from feed.tag_follow import TagFollow

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
    db.session.commit()


