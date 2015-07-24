# -*- coding: utf-8 -*-
'''API.'''
from flask_restful import Resource, reqparse, fields, marshal

from modori.extensions import api
from modori.controllers.nlp import NLP

from .apifields import *


#MECAB
@api.resource('/api/pos', endpoint='pos')
class POSAPI(Resource):

	def __init__(self):
		self.req = reqparse.RequestParser()
		self.req.add_argument('text', type=str, help='no text provided', location="json")
		super(POSAPI, self).__init__()

	def get(self):
		result = NLP.pos("test")
		return result
	def post(self):
		args = self.req.parse_args()
		result = NLP.pos(args.text)
		return result

@api.resource('/api/nouns', endpoint='nouns')
class NounsAPI(Resource):
	def __init__(self):
		self.req = reqparse.RequestParser()
		self.req.add_argument('text', type=str, help='no text provided', location="json")
		super(NounsAPI, self).__init__()
	def get(self):
		result = NLP.nouns("test")
	def post(self):
		args = self.req.parse_args()
		result = NLP.nouns(args.text)
		return result

@api.resource('/api/morphs', endpoint='morphs')
class MorphsAPI(Resource):
	def __init__(self):
		self.req = reqparse.RequestParser()
		self.req.add_argument('text', type=str, help='no text provided', location="json")
		super(MorphsAPI, self).__init__()
	def get(self):
		result = NLP.morphs("test")
	def post(self):
		args = self.req.parse_args()
		result = NLP.morphs(args.text)
		return result