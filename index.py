import os
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('moodview.html')

@app.route('/question')
def question():
    return render_template('question.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

