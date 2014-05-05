import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import json
from collections import namedtuple as NT
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Photos.db'
db = SQLAlchemy(app)

class Photo(db.Model):
	__tablename__ = "Photos"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	img_path = db.Column(db.String(120), unique=True)
	mscore = db.Column(db.Integer)


	def __init__(self, name, img_path, mscore):
		self.name = name
		self.img_path = img_path
		self.mscore = mscore
		
@app.route('/', methods=['POST', 'GET'])
@app.route('/question', methods=['POST', 'GET'])
def question():
	if request.method == 'POST':
		counter = 0
		for fnum, item in request.form.items():
			counter = counter + int(item) 
			print counter
		return redirect('/simple_view.html/'+str(counter))
	return render_template('question.html')

@app.route('/simple_view.html')
@app.route('/simple_view.html/<data>')
def view(data=None):
	temp = Photo.query.all()
	dat = None
	for item in temp:
		if int(item.mscore) == int(data):
			dat = item.img_path
		print item.mscore
		print item.img_path
	tempp = str(dat)
	print tempp
	return render_template('simple_view.html', image_path=dat)

if __name__ == '__main__':
    app.run(debug=True)
