import unittest
import os
from selenium import webdriver

class C9Demo(unittest.TestCase):
    def setUp(self):
        chromedriver = '../drivers/chromedriver'
        os.environ['webdriver.chrome.driver'] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.maximize_window()
        self.driver.get('http://selenium-testing-winwust.c9users.io/search.html')

    def test_find_by_class_name(self):
        element = self.driver.find_element_by_class_name('label')
        self.assertEqual(element.text, 'Search')

    def test_find_by_name(self):
        element = self.driver.find_element_by_name('keyword')
        self.assertEqual(element.get_attribute('value'), 'Type in your keyword')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main()
