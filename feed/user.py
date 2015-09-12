import uuid
from feed import db, bcrypt
from flask.ext.restful import Resource
from flask import jsonify, request

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    photo_url = db.Column(db.String(256), unique=True)
    role = db.Column(db.String(256), unique=True)
    score = db.Column(db.Integer)
    token = db.Column(db.String(256), unique=True)

    def __init__(self, email, password = '', role = '', photo_url='', score=0, token=''):
        self.email = email
        self.password = password
        self.role = role
        self.photo_url = photo_url
        self.score = score
        self.token = token

    def __repr__(self):
        return '<User %r>' % self.email
    
    def set_password(self, plaintext):
        self.password = bcrypt.generate_password_hash(plaintext)

    def verify_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)
    
    def set_token(self,):
        self.token = uuid.uuid4()

class UserApi(Resource):                                                      
    def get(self):
        admin = User.query.filter_by(role='admin').first()                             
        if not admin:                                                                  
            return {False}
        return {'email': admin.email, 'name' : admin.username}

    def post(self):
        print request.form
        email=request.form['email']
        password = request.form['password']
        if email and password:
            user = User.query.filter_by(email=email).first()
            if not user:
                user = User(email, email)
                user.set_password(password)
                user.set_token()
                db.session.add(user)
                
            return jsonify(email= user.email, token= user.token)
                
