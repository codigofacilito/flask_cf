#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import flash
from flask import g
from flask import url_for
from flask import redirect

from config import DevelopmentConfig

from flask_wtf import CsrfProtect
import forms
import json

from models import User
from models import Comment
from models import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect()

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.before_request
def before_request():
	if 'username' not in session and request.endpoint in ['comment']:
		return redirect(url_for('login'))

	elif 'username' in session and request.endpoint in ['login', 'create']:
		return redirect(url_for('index'))		
		

@app.after_request
def after_request(response):
	return response

@app.route('/')
def index():
	if 'username' in session:
		username = session['username']
		print username
	title = 'Index'
	return render_template('index.html', title = title)

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
	return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
	login_form = forms.LoginForm(request.form)
	if request.method == 'POST' and login_form.validate():
		username = login_form.username.data
		password = login_form.password.data

		user = User.query.filter_by(username = username).first()
		if user is not None and user.verify_password(password):
			success_message = 'Bienvenido {}'.format(username)
			flash(success_message)
			session['username'] = username
			session['id'] = user.id
			return redirect( url_for('index') )

		else:
			error_message= 'Usuario o password no validos!'
			flash(error_message)

		session['username'] = login_form.username.data
	return render_template('login.html', form = login_form)

@app.route('/comment', methods = ['GET', 'POST'])
def comment():
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():

		user_id = session['id']
		comment = Comment(text = comment_form.comment.data, user_id = user_id)
		db.session.add(comment)
		db.session.commit()
		
	else:
		print "Error en el formulario"

	title = "Curso Flask"
	return render_template('comment.html', title = title, form = comment_form)

@app.route('/create', methods = ['GET', 'POST'])
def create():
	create_form = forms.CreateForm(request.form)
	if request.method == 'POST' and create_form.validate():
		user = User( 	create_form.username.data,
									create_form.password.data,
									create_form.email.data )

		db.session.add(user)  
		db.session.commit()

		success_message = 'Usuario registrado en la base de datos'
		flash(success_message)

	return render_template('create.html', form = create_form)

@app.route('/cookie')
def cookie():
	reponse = make_response( render_template('cookie.html') )
	reponse.set_cookie('custome_cookie', 'Eduardo')
	return reponse

@app.route('/ajax-login', methods= ['POST'])
def ajax_login():
	print request.form
	username = request.form['username']
	response = { 'status': 200, 'username': username, 'id': 1 }
	return  json.dumps(response)

if __name__ == '__main__':
	csrf.init_app(app)
	db.init_app(app)

	with app.app_context():
		db.create_all()

	app.run(port=8000)

