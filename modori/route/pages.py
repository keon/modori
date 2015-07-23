# -*- coding: utf-8 -*-
from flask import (Blueprint, render_template, jsonify)

page = Blueprint('page', __name__, static_folder="../static")


#only receives the following headers
@page.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response

#every path leads to index.html
@page.route('/')
def home(*args, **kwargs):
    return render_template('index.html')

@page.route('/<path:p>')
def pageNotFound(*args, **kwargs):
	return render_template('404.html')

#api 를 찾을 수 없으면
@page.route('/api/<path:p>')
def apiNotFound(*args, **kwargs):
    return jsonify({"type":"404", "message":"api not found"})


#DOCUMENTATION
@page.route('/docs')
def docshome():
	return render_template('docs.html')