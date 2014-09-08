"""
Justin Welenofsky's functional tests for the django official tutorial
Date: September 8, 2014
"""

from selenium import webdriver

import unittest

import time

class NewUserTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_access_root(self):
		self.browser.get('http://localhost:8000')
		html = self.browser.find_element_by_tag_name('html').text
		self.assertIn('It worked!', html)
