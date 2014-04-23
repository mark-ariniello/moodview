import os
from flask import Flask
from flask import request
from flask import render_template
from flask import json
from collections import namedtuple as NT
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
db = SQLAlchemy(app)

class Photo(db.Model):
	tablename = "photos"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	img_path = db.Column(db.String(120), unique=True)


	def __init__(self, name, img_path):
		self.name = name
		self.img_path = img_path

@app.route('/')
@app.route('/question')
def question():
    return render_template('question.html')
@app.route('/simple_view.html')
def view():
	return render_template('simple_view.html')

if __name__ == '__main__':
    app.run(debug=True)
