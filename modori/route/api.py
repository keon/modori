# -*- coding: utf-8 -*-
'''Public section, including homepage and signup.'''
from flask import (Blueprint, request, abort, render_template, url_for, jsonify, g)
from flask_restful import Resource, reqparse, fields, marshal

from modori.extensions import api

from .apifields import *

from datetime import datetime
import types

from konlpy.tag import Mecab

mecab = Mecab()



mod = Blueprint('rest', __name__, static_folder="../static")


#only receives the following headers
@mod.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

#every path leads to index.html
@mod.route('/')
@mod.route('/<path:p>')
def home(*args, **kwargs):
    return render_template('index.html')


#MECAB
@api.resource('/api/mecab', endpoint='mecab')
class MecabAPI(Resource):
    def __init__(self):
        pass
    def get(self):
        test = "testt"
        return mecab.morphs(u'영등포구청역에 있는 맛집 좀 알려주세요.') #marshal(test, test_fields)