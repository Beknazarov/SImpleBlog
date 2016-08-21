import unittest
from unittest import TestCase

import json

from db.database import DataAccessLayer

JSON_FILE_DIR = '/home/kinglight/PycharmProjects/Test/AttractorWebServer/data_json/'


def get_json_value():
    with open(JSON_FILE_DIR + 'db_test_data.json', 'r') as f:
        return json.load(f)


def createMultipleUser(db_object):
    try:
        decoded = get_json_value()

        for x in decoded['user']:
            db_object.create_user(username=x['username'], password=x['password'], email=x['email'])
    except (ValueError, KeyError, TypeError):
        print("JSON format error")


def createMultiplePost(db_object):
    try:
        decoded = get_json_value()

        for x in decoded['post']:
            print(x['username'])
            db_object.create_post(username=x['username'], title=x['title'], description=x['description'])
    except (ValueError, KeyError, TypeError):
        print("JSON format error")


class TestDataAccessLayer(TestCase):
    def setUp(self):
        self.db = DataAccessLayer()
        createMultipleUser(self.db)
        createMultiplePost(self.db)

    def test_user_is_exist(self):
        username = "nurs"
        self.assertEqual(username, self.db.test_get_username_by_id(1))

    @unittest.expectedFailure
    def test_check_count_post(self):
        count = self.db.count_post()
        self.assertEqual(5, count)

    def tearDown(self):
        pass
