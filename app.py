from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import passlib
from passlib.hash import pbkdf2_sha256
import socket
import os
from identicons import *

location = os.path.join('static','identicons')
location2 = os.path.join('static','identicons_user_side')

app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User Credentials'
app.config['SQLALCHEMY_BINDS'] = {
    'db': 'sqlite:///User Credentials',
    'db1': 'sqlite:///User Credentials_ Browser side'
}
app.config['upload']=location
app.config['upload_user_side']=location2

db=SQLAlchemy(app)

class User(db.Model):
    __bind_key__='db'
    __tablename__="User details"
    _id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(500), nullable=False)

    def __init__(self, name, email, password):
        self.name=name
        self.email=email
        self.password=password

class User1(db.Model):
    __bind_key__='db1'
    __tablename__="User details - Browser"
    _id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(500), nullable=False)

    def __init__(self, name, email, password):
        self.name=name
        self.email=email
        self.password=password

def getip():
    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname)
    return ip

def getsalt(password):
    salt_used=password[21:43]
    salt_decoded=passlib.utils.binary.ab64_decode(salt_used)
    return salt_decoded

def get_user_cred(given_salt, given_pass):
    ip=getip()
    user_pass=str(ip)+given_pass
    hash=pbkdf2_sha256.using(salt=given_salt).hash(user_pass)
    return hash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sign_in', methods=['GET', 'POST'])
def signin():
    if request.method=='POST':
        user_email=request.form['email']
        check=User.query.filter_by(email=user_email).first()
        check1=User1.query.filter_by(email=user_email).first()
        if check is None:
            return render_template('sign_in.html', message="No such email id")
        else:
            found_user_email = check.email
            found_user_pass = check.password
            salt_bytes=getsalt(found_user_pass)
            passo=check1.password
            emailo=check1.email
            hashed_user_side=get_user_cred(salt_bytes,passo)
            full_location = os.path.join(app.config['upload'], found_user_email)
            full_location2 = os.path.join(app.config['upload_user_side'], emailo)
            generate_identicon(found_user_pass, found_user_email, full_location)
            image_address="/"+full_location+".png"
            generate_identicon(hashed_user_side,emailo,full_location2)
            image_address2="/"+full_location2+".png"
            return render_template('sign_in2.html', message="", address=image_address, address2=image_address2)

    else:
        return render_template('sign_in.html')
    return render_template('sign_in.html')

@app.route('/signup')
def signup_load():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        user_name=request.form['name']
        user_email=request.form['email']
        user_passw=request.form['password']
        check=User.query.filter_by(email=user_email).first()
        if check is not None:
            return render_template('signup.html', message="This email already exists")
        else:
            ip=getip()
            user_pass=str(ip)+user_passw
            user_password=pbkdf2_sha256.hash(user_pass)
            collected_data=User(user_name, user_email, user_password)
            collected_data1=User1(user_name, user_email, user_passw)
            db.session.add(collected_data)
            db.session.commit()
            db.session.add(collected_data1)
            db.session.commit()
            message="You have successfully signed up !"
            return render_template('result.html', message=message)
    else:
        message="Sign Up failed. Try again"
        return render_template('result.html', message=message)

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
