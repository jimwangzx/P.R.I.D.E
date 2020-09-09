from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import hashlib
from passlib.hash import pbkdf2_sha256
import socket
from identicons import *
import os

location = os.path.join('static','identicons')

app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User Credentials'
app.config['upload']=location

db=SQLAlchemy(app)

class User(db.Model):
    __tablename__="User details"
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
    global ip
    ip=socket.gethostbyname(hostname)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sign_in', methods=['GET', 'POST'])
def signin():
    if request.method=='POST':
        user_email=request.form['email']
        check=User.query.filter_by(email=user_email).first()
        if check is None:
            return render_template('sign_in.html', message="No such email id")
        else:
            found_user_email = check.email
            found_user_pass = check.password
            full_location = os.path.join(app.config['upload'], found_user_email)
            generate_identicon(found_user_pass, found_user_email, full_location)
            image_address="/"+full_location+".png"
            return render_template('sign_in.html', message="Email exists. Proceed", address=image_address)

    else:
        return render_template('sign_in.html')



    return render_template('sign_in.html')

@app.route('/users')
def users():
    return render_template('users.html')

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
            getip()
            user_pass=str(ip)+user_passw
            user_password=pbkdf2_sha256.hash(user_pass)
            collected_data=User(user_name, user_email, user_password)
            db.session.add(collected_data)
            db.session.commit()
            message="You have successfully signed up !"
            return render_template('result.html', message=message)
    else:
        message="Sign Up failed. Try again"
        return render_template('result.html', message=message)

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
