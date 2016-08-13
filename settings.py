# -- coding: utf-8 --
import os

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
STATIC_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
JSON_FILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'json')
# import json
# from settings import JSON_FILE_DIR
# from pprint import pprint
#
# json_input = '{"persons": [{"name": "Brian", "city": "Seattle"}, {"name": "David", "city": "Amsterdam"} ] }'
#
# with open(JSON_FILE_DIR + '/db_test_data.json') as data_file:
#     data = json.load(data_file)
#
# pprint(data)
#
# try:
#     decoded = json.loads(json_input)
#
#     # Access data
#     for x in decoded['persons']:
#         print(x['name'])
#
# except (ValueError, KeyError, TypeError):
#     print("JSON format error")
#
