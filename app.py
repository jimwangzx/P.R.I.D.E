from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.sqlite3'

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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin')
def singin():
    return render_template('signin.html')

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
        user_pass=request.form['password']

        collected_data=User(user_name, user_email, user_pass)
        db.session.add(collected_data)
        db.session.commit()
        return render_template('signup.html')
    else:
        return render_template('signup.html')

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
