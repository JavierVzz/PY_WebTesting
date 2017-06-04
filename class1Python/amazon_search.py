import unittest
import os
from selenium import webdriver

class AmazonSearch(unittest.TestCase):

	def setUp(self):
		chromedriver = '../drivers/chromedriver'
		os.environ['webdriver.chrome.driver'] = chromedriver
		self.driver = webdriver.Chrome(chromedriver)
		self.driver.maximize_window()
		self.driver.get('https://www.amazon.com/')

	def test_amazon_search(self):
		element = self.driver.find_element_by_id('twotabsearchtextbox')
		element.clear()
		element.send_keys('Selenium Webdriver')
		search_icon = self.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
		search_icon.click()

		self.assertEqual(self.driver.find_element_by_id('s-result-count').text,
						 '1-16 of 73 results for "Selenium Webdriver"')

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
