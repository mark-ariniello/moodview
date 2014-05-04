import os
import cgi
from flask import Flask
from flask import request
from flask import render_template
from flask import json
from collections import namedtuple as NT
from flask.ext.sqlalchemy import SQLAlchemy
import cgitb
cgitb.enable()

v = int
v1 = int
v2 = int
v3 = int
v4 = int
v5 = int

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
db = SQLAlchemy(app)

class Photo(db.Model):
	tablename = "Photos"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	img_path = db.Column(db.String(120), unique=True)


	def __init__(self, name, img_path):
		self.name = name
		self.img_path = img_path
@app.route('/')
@app.route('/question')
def question():
	form = cgi.FieldStorage()
        v1 = form.getvalue("hi")
        v2 = form.getvalue("waveh")
        v3 = form.getvalue("waves")
        v4 = form.getvalue("what")
        v5 = form.getvalue("ignore")

        v = v1 + v2 + v3 + v4 + v5;
        print v  
	return render_template('question.html')

@app.route('/simple_view.html')
@app.route('/simple_view.html/<data>')
def view(data=None):
#	temp = Photos.query.all()
#	print temp
#	dat = None
#	for item in temp:
#		if item.id == data:
#			dat = item.imge_path
	return render_template('simple_view.html')


if __name__ == '__main__':
    app.run(debug=True)
