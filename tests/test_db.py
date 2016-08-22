import unittest
from unittest import TestCase

import json

from db.database import DataAccessLayer

db = DataAccessLayer()
JSON_FILE_DIR = '/home/kinglight/PycharmProjects/Test/AttractorWebServer/data_json/'


def get_json_value():
    with open(JSON_FILE_DIR + 'db_test_data.json', 'r') as f:
        return json.load(f)


def create(db_object):
    try:
        decoded = get_json_value()

        for user in decoded['user']:
            db_object.create_user(username=user['username'], password=user['password'], email=user['email'])
        for post in decoded['post']:
            db_object.create_post(username=post['author'], title=post['title'], description=post['description'])
    except (ValueError, KeyError, TypeError):
        print("JSON format error")


class TestDataAccessLayer(TestCase):
    def setUp(self):
        self.db = DataAccessLayer()
        create(self.db)

    def test_user_is_exist(self):
        username = "nurs"
        self.assertEqual(username, self.db.test_get_username_by_id(1))

    @unittest.expectedFailure
    def test_check_count_post(self):
        count = self.db.count_post()
        self.assertEqual(5, count)

    def tearDown(self):
        pass
