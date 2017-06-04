import unittest
import os
from selenium import webdriver

class C9Demo(unittest.TestCase):
    def setUp(self):
        chromedriver = '../drivers/chromedriver'
        os.environ['webdriver.chrome.driver'] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.maximize_window()
        self.driver.get('http://selenium-testing-winwust.c9users.io/links.html')

    def test_find_link_by_text(self):
        element = self.driver.find_element_by_link_text('Facebook')
        self.assertEqual(element.get_attribute('href'), 'https://www.facebook.com/')

    def test_find_link_by_partial_text(self):
        element = self.driver.find_element_by_partial_link_text('Digg')
        self.assertEqual(element.get_attribute('href'), 'http://www.digg.com/')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main()
