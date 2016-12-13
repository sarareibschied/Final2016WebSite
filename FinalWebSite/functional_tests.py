# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		if os.name=='nt':
			self.browser = webdriver.Chrome()
		else:
			self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_home_page(self):
		self.browser.get('http://localhost:8000/index.html')

		# when we are on the home page, the page title says "The Mandelbrot Set"
		self.assertIn("The Mandelbrot Set",self.browser.title)

		h=self.browser.find_element_by_tag_name('h1')

		m=self.browser.find_element_by_tag_name('img')
		self.assertIn('M.jpg',m.get_attribute('src'))

		a=self.browser.find_element_by_id('circular')
		a.click()

		self.assertIn('The Code',self.browser.title)
		
		h=self.browser.find_element_by_tag_name('h1')
		
		m=self.browser.find_element_by_tag_name('img')
		self.assertIn('mbrot.png',m.get_attribute('src'))

		a=self.browser.find_element_by_id('bigcircle')
		a.click()

		self.assertIn("The Mandelbrot Set",self.browser.title)

		

		

		

		

		
		

if __name__=="__main__":
		unittest.main(warnings="ignore")

