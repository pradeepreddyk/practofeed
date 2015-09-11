from feed import db
from flask.ext.restful import Resource

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    photo_url = db.Column(db.String(256), unique=True)
    role = db.Column(db.String(256), unique=True)
    score = db.Column(db.Integer)

    def __init__(self, username, email, role = '', photo_url='', score=0):
        self.username = username
        self.email = email
        self.role = role
        self.photo_url = photo_url
        self.score = score

    def __repr__(self):
        return '<User %r>' % self.username

class UserApi(Resource):                                                      
    def get(self):
        admin = User.query.filter_by(role='admin').first()                             
        if not admin:                                                                  
            return {False}
        return {'email': admin.email, 'name' : admin.username}
