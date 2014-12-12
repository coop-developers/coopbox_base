# -*- coding: utf-8 -*-
from django_jinja import library
import json

jsonify = library.filter(name='jsonify', fn=json.dumps)
