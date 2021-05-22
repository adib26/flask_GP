from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/ed-site'

db = SQLAlchemy(app)

class User(db.Model):
    type = db.Column(db.Integer())
    username = db.Column(db.String(20),primary_key=True,unique=True)
    password = db.Column(db.String(30),unique=True)
    email = db.Column(db.String(20),unique=True)
    Fname = db.Column(db.String(20))
    Lname = db.Column(db.String(20))
    courses = db.relationship('Courses',backref='course',lazy=True)
    SIC = db.relationship('StudentsInCourses',backref='sic',lazy=True)
    #SIC = db.relationship('StudentsInCourses',backref='sic',lazy=True)


class Courses(db.Model):
    #id = db.Column(db.Integer(),primary_key=True)
    CourseName = db.Column(db.String(40),primary_key=True)  
    Iusername = db.Column(db.String(20),db.ForeignKey('user.username'))
    courname = db.relationship('StudentsInCourses',backref='courssename',lazy=True)

class StudentsInCourses(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    coursename =  db.Column(db.String(40),db.ForeignKey('courses.CourseName'))
    #Iusername = db.Column(db.String(20),db.ForeignKey('courses.Iusername'))
    Susername = db.Column(db.String(20),db.ForeignKey('user.username'))

from app import models
from app import views


