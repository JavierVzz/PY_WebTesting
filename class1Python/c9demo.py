import unittest
import os
from selenium import webdriver

class C9Demo(unittest.TestCase):
    def setUp(self):
        chromedriver = '../drivers/chromedriver'
        os.environ['webdriver.chrome.driver'] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.maximize_window()
        self.driver.get('http://webapptestingspring2017-winwust.c9users.io/helloworld.html')

    def test_find_by_id(self):
        element = self.driver.find_element_by_id('title')
        self.assertEqual(element.text, 'Hello World')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main()
