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

    def test_find_links_with_target_attr(self):
        links = self.driver.find_elements_by_xpath('//*[@target]')
        self.assertEqual(len(links), 2)
        expected_urls = ['https://www.google.com/', 'http://www.msn.com/']
        actual_urls = list(map(lambda link: link.get_attribute('href'), links))
        self.assertListEqual(expected_urls, actual_urls)

    def test_find_links_that_open_new_window(self):
        link = self.driver.find_element_by_xpath('//a[@target="_blank"]')
        self.assertEqual(link.text, 'MSN Link')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main()
