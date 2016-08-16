import unittest
from unittest import TestCase

from db.database import DataAccessLayer, Post

import json


def get_post_array():
    with open('/home/kinglight/PycharmProjects/AttractorWebServer/json_dir/db_test_data.json', 'r') as f:
        return json.load(f)


class TestDataAccessLayer(TestCase):
    def setUp(self):
        self.db = DataAccessLayer()
        username = "Nursultan"
        password = "12345"
        phone = "0553687887"
        address = "Partizanskaya 12"
        email = "beknazarovnursultan@gmail.com"
        self.db.CreateUser(username=username, password=password, phone=phone, address=address, email=email)

    def test_create_multiple_post(self):

        try:
            decoded = get_post_array()

            for x in decoded['post']:
                self.db.CreatePost(id=x['id'], title=x['title'], description=x['description'], like=x['like'],
                                   author=x['author'])
        except (ValueError, KeyError, TypeError):
            print("JSON format error")
        self.assertEqual(Post.idList[0], 1)

    def test_user(self):
        username = "Nursultan"
        self.assertEqual(username, self.db.GetUserAttribute().name[0])

    @unittest.expectedFailure
    def test_check_count_post(self):
        count = self.db.count_post()
        self.assertEqual(5, count)

    def test_auth_user(self):
        self.assertTrue(self.db.CheckUserIsExist("Nursultan", "12345"))

    def test_check_user_post(self):
        author = "user"
        id = 1
        self.assertTrue(not self.db.CheckUserPost(author, id))

    def tearDown(self):
        pass
