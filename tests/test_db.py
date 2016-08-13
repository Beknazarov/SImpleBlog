import unittest
from unittest import TestCase

from db.database import DataAccessLayer


class TestDataAccessLayer(TestCase):
    def setUp(self):
        self.db = DataAccessLayer()
        username = "Nursultan"
        password = "12345"
        phone = "0553687887"
        address = "Partizanskaya 12"
        email = "beknazarovnursultan@gmail.com"
        self.db.CreateUser(username=username, password=password, phone=phone, address=address, email=email)
        id = 1
        title = 'New York'
        description = 'USA country'
        like = 5
        author = username
        self.db.CreatePost(id=id, title=title, description=description, like=like, author=author)

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
        author = "Nursultan"
        id = 1
        self.assertTrue(self.db.CheckUserPost(author, id))

    def tearDown(self):
        pass
