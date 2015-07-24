# -*- coding: utf-8 -*-
'''API.'''
from flask_restful import Resource, reqparse, fields, marshal

from modori.extensions import api

from .apifields import *


#MECAB
@api.resource('/api/mecab', endpoint='mecab')
class MecabAPI(Resource):
    def __init__(self):
        pass
    def get(self):
        test = "testt"
        return marshal(test, test_fields)