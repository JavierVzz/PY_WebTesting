import unittest
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class C9Demo(unittest.TestCase):
    def setUp(self):
        chromedriver = '../drivers/chromedriver'
        os.environ['webdriver.chrome.driver'] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.maximize_window()
        self.driver.get('http://selenium-testing-winwust.c9users.io/divs.html')

    def test_find_by_xpath(self):
        id1 = self.driver.find_element_by_id('id1')
        p2 = id1.find_element_by_xpath('./p')
        self.assertEqual(p2.text, 'World')
        p3 = id1.find_element_by_xpath('//p')
        self.assertEqual(p3.text, 'Hello')
        p4 = id1.find_element_by_xpath('.//p')
        self.assertEqual(p4.text, 'World')

    def test_find_by_xpath_with_exception(self):
        id1 = self.driver.find_element_by_id('id1')
        with self.assertRaises(NoSuchElementException):
            id1.find_element_by_xpath('/p')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main()
