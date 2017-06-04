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

    def test_find_ul(self):
        element = self.driver.find_element_by_xpath('//ul')
        self.assertEqual(element.get_attribute('id'), 'list1')

    def test_find_lis(self):
        lis = self.driver.find_elements_by_xpath('//li')
        self.assertEqual(len(lis), 8)
        lis2 = self.driver.find_elements_by_xpath('//ul/li')
        self.assertEqual(len(lis2), 7)
        lis3 = self.driver.find_elements_by_xpath('//ul//li')
        self.assertEqual(len(lis3), 8)

    def test_find_lis_inside_ul(self):
        ul = self.driver.find_element_by_id('list2')
        lis = ul.find_elements_by_tag_name('li')
        self.assertEqual(len(lis), 3)
        lis2 = self.driver.find_elements_by_tag_name('li')
        self.assertEqual(len(lis2), 8)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main()
