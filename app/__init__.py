from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)

from app import views

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/ed-site'

db = SQLAlchemy(app)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'ed-site'

#db = MySQL(app)

class Students(db.Model):
    username = db.Column(db.String(20),primary_key=True,unique=True)
    password = db.Column(db.String(30),unique=True)
    email = db.Column(db.String(20),unique=True)
    Fname = db.Column(db.String(20))
    Lname = db.Column(db.String(20))
    def __rep__(self):
        return f"User('{self.username}','{self.password}')"


class Instructor(db.Model):
    username = db.Column(db.String(20),primary_key=True,unique=True)
    password = db.Column(db.String(30),unique=True)
    email = db.Column(db.String(20),unique=True)
    Fname = db.Column(db.String(20))
    Lname = db.Column(db.String(20))
    courses = db.relationship('Courses',backref='course',lazy=True)
    def __rep__(self):
        return f"User('{self.username}','{self.password}')"

class Courses(db.Model):
    CourseName = db.Column(db.String(40))
    id = db.Column(db.Integer(),primary_key=True)
    Iusername = db.Column(db.String(20),db.ForeignKey('instructor.username'))


    def __rep__(self):
        return  '<TUser %r>' % self.Iusername + '  <cour %r>' % self.CourseName


