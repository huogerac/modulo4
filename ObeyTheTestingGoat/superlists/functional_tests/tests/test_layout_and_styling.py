from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LayoutAndStylingTest(FunctionalTest):

	def test_layout_and_styling(self):
		# Edith goes to the home page
		self.browser.get(self.server_url)

		# She notices the input box is nicely centered
		inputbox = self.browser.find_element_by_tag_name('input')
		#inputbox = self.get_item_input_box()
		window_width = self.browser.get_window_size()['width']
		#self.assertAlmostEqual(
		#	inputbox.location['x'] + inputbox.size['width'] / 2,
		#	window_width / 2,
		#	delta=3
		#)	
