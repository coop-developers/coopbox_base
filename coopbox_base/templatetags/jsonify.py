# -*- coding: utf-8 -*-
from django.conf import settings
from django_jinja import library
import json

jsonify = library.filter(name='jsonify', fn=json.dumps)
