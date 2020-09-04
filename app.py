from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import hashlib
from passlib.hash import pbkdf2_sha256
import socket

app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User Credentials'

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

@app.route('/sign_in')
def singin():
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

        getip()
        user_pass=str(ip)+user_passw

        user_email=pbkdf2_sha256.hash(user_email)
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
