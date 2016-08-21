import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from db.database import DataAccessLayer


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.db = DataAccessLayer()

    def test_authenticated_user(self):

        self.driver.get("http://127.0.0.1:8080/register/")
        username = self.driver.find_element_by_name("username")
        username.send_keys("nurs")

        password = self.driver.find_element_by_name("password")
        password.send_keys("12345")
        email = self.driver.find_element_by_name("email")
        email.send_keys("nurs@gmail.com")

        self.db.create_user(username.get_attribute('value'), password.get_attribute('value'),
                            email.get_attribute('value'))
        self.assertEqual("nurs", self.db.test_get_username_by_id(1))
        btn_register = self.driver.find_element_by_css_selector('input[type="submit"]')
        btn_register.click()
        btn_go = self.driver.find_element_by_css_selector('a[href="/admin/"]')
        btn_go.click()
        username_login = self.driver.find_element_by_name("username")
        username_login.send_keys("nurs")
        password_login = self.driver.find_element_by_name("password")
        password_login.send_keys("12345")
        # print(self.driver.)
        btn_login = self.driver.find_element_by_css_selector('input[type="submit"]')
        btn_login.click()
        # def tearDown(self):
        #     self.driver.close()


