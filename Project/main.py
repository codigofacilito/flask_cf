#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session

from flask import url_for
from flask import redirect

from flask_wtf import CsrfProtect
import forms

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

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

@app.route('/cookie')
def cookie():
	reponse = make_response( render_template('cookie.html') )
	reponse.set_cookie('custome_cookie', 'Eduardo')
	return reponse

@app.route('/login', methods = ['GET', 'POST'])
def login():
	login_form = forms.LoginForm(request.form)
	if request.method == 'POST' and login_form.validate():
		session['username'] = login_form.username.data
	return render_template('login.html', form = login_form)

@app.route('/comment', methods = ['GET', 'POST'])
def comment():
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		print comment_form.username.data
		print comment_form.email.data
		print comment_form.comment.data
	else:
		print "Error en el formulario"

	title = "Curso Flask"
	return render_template('comment.html', title = title, form = comment_form)

if __name__ == '__main__':
	app.run(debug=True, port=8000)
