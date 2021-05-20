from app import app
from flask import Flask,render_template,url_for





@app.route('/')
def index():
    return render_template('homepage.html')



@app.route('/instructor/home/')
def instructor_home():
    return render_template('homepage.html')