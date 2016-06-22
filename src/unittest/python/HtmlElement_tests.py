from mockito import mock, verify
import unittest

from html_element import html_element
from buildHTML import Html_Builder
from HTML import HTML

class HtmlElementTest(unittest.TestCase):
	# @classmethod
	# def setUpClass(self):
		# element = html_element()
	def test_string_output_of_html_element(self):
		# element = html_element()
		self.assertEqual("", "")
	def test_html_element_string_is_blank_initially(self):
		element = html_element()
		string = element.__str__()
		self.assertEqual(string, "")
		
	def test_html_element_dict_is_empty_unless_specified(self):
		element = html_element()
		dict = element.meta_dict
		blank_dict = {}
		self.assertEqual(blank_dict, dict)
		
	def test_html_element_has_none_text_unless_specified(self):
		element = html_element()
		text = element.text
		self.assertEqual(None, text)
	
	def test_html_element_string_without_attributes_not_nested(self):
		element = html_element(False, "a", "Anchor")
		string = element.__str__()
		self.assertEqual("<a>Anchor</a>\n", string)
	
	def test_html_element_string_without_attributes_nested_no_level(self):
		element = html_element(True, "a", "Anchor")
		string = element.__str__()
		self.assertEqual("<a>Anchor</a>\n", string)
		
	def test_html_element_string_without_attributes_nested_with_level(self):
		element = html_element(True, "a", "Anchor")
		element.nested_level = 1
		string = element.__str__()
		self.assertEqual("\t<a>Anchor</a>\n", string)
		
	def test_html_element_string_with_attributes_not_nested(self):
		temp_dict = {'href': 'http://www.google.com'}
		temp_test = temp_dict['href']
		self.assertEqual('http://www.google.com', temp_test)
		element = html_element(False, "a", "Anchor", 0, temp_dict)
		temp_attr = element.meta_dict
		self.assertEqual(temp_dict, temp_attr)
		string = element.__str__()
		self.assertEqual("<a href='http://www.google.com'>Anchor</a>\n", string)
		
	def test_html_element_string_with_attributes_nested_no_level(self):
		temp_dict = {'href': 'http://www.google.com'}
		temp_test = temp_dict['href']
		self.assertEqual('http://www.google.com', temp_test)
		element = html_element(True, "a", "Anchor", 0, temp_dict)
		string = element.__str__()
		self.assertEqual("<a href='http://www.google.com'>Anchor</a>\n", string)
	def test_html_element_string_with_attributes_nested_with_level(self):
		temp_dict = {'href': 'http://www.google.com'}
		temp_test = temp_dict['href']
		self.assertEqual('http://www.google.com', temp_test)
		element = html_element(True, "a", "Anchor", 0, temp_dict)
		element.nested_level = 1
		string = element.__str__()
		self.assertEqual("\t<a href='http://www.google.com'>Anchor</a>\n", string)
		
	def test_empty_html_object(self):
		html_obj = HTML()
		self.assertFalse(html_obj.is_full_html)
		self.assertFalse(html_obj.has_body)
		self.assertFalse(html_obj.has_head)
		temp_list = []
		self.assertEqual(temp_list, html_obj.element_list)
		self.assertEqual("", html_obj.html_string)
		self.assertEqual(0, html_obj.inc_id)
		
	def test_html_object_string_method(self):
		html_obj = HTML()
		blank_string = html_obj.__str__()
		self.assertEqual("", blank_string)
		
	def test_html_object_element_list(self):
		html_obj = HTML()
		empty_list = html_obj.get_element_list()
		test_list = []
		self.assertEqual(test_list, empty_list)
		
	def test_html_object_get_element(self):
		html_obj = HTML()
		test_element = html_element()
		html_obj.add_element(test_element)
		self.assertEqual(test_element, html_obj.get_element(0))
		
	def test_html_object_get_nested_level(self):
		html_obj = HTML()
		self.assertEqual(0, html_obj.get_top_element_nested_level())
	
	def test_html_object_get_nested_level_with_element_list(self):
		html_obj = HTML()
		test_element = html_element()
		html_obj.add_element(test_element)
		html_obj.set_element_nested_level(0, 1)
		self.assertEqual(1, html_obj.get_top_element_nested_level())
		
	def test_html_object_set_nested_level(self):
		html_obj = HTML()
		test_element = html_element()
		html_obj.add_element(test_element)
		html_obj.set_element_nested_level(0, 1)
		self.assertEqual(1, html_obj.get_element(0).nested_level)
	
	def test_html_object_set_element(self):
		html_obj = HTML()
		test_element = html_element()
		html_obj.add_element(test_element)
		swap_element = html_element(False, "a", "Anchor")
		html_obj.set_element(0, swap_element)
		self.assertEqual(swap_element, html_obj.get_element(0))
		
	def test_html_object_full_html(self):
		html_obj = HTML()
		html_obj.change_full_html()
		self.assertEqual(True, html_obj.is_full_html)
		
	def test_html_object_has_body(self):
		html_obj = HTML()
		html_obj.change_has_body()
		self.assertEqual(True, html_obj.has_body)
		
	def test_html_object_generate_empty_html(self):
		html_obj = HTML()
		html_obj.generate_html()
		self.assertEqual("", html_obj.html_string)
		
	def test_html_object_generate_full_html_no_body(self):
		html_obj = HTML(True)
		html_obj.generate_html()
		self.assertEqual("<!DOCTYPE html>\n <html>\n</html>", html_obj.html_string)
		
	def test_html_object_generate_full_html_with_body(self):
		html_obj = HTML(True, True)
		html_obj.generate_html()
		self.assertEqual("<!DOCTYPE html>\n <html>\n<body>\n</body>\n</html>", html_obj.html_string)
	
	def test_html_object_generate_full_html_with_body_and_head(self):
		html_obj = HTML(True, True, True)
		html_obj.generate_html()
		self.assertEqual("<!DOCTYPE html>\n <html>\n<head>\n</head>\n<body>\n</body>\n</html>", html_obj.html_string)
	
	def test_html_object_generate_full_html_with_body_head_and_elements(self):
		html_obj = HTML(True, True, True)
		test_element = html_element(False, "a", "Anchor")
		html_obj.add_element(test_element)
		html_obj.generate_html()
		self.assertEqual("<!DOCTYPE html>\n <html>\n<head>\n</head>\n<body>\n<a>Anchor</a>\n</body>\n</html>", html_obj.html_string)
		
	def test_html_object_generate_full_html_no_body_with_elements(self):
		html_obj = HTML(True, False, False)
		test_element = html_element(False, "a", "Anchor")
		html_obj.add_element(test_element)
		html_obj.generate_html()
		self.assertEqual("<!DOCTYPE html>\n <html>\n<a>Anchor</a>\n</html>", html_obj.html_string)
		
	def test_html_object_generate_not_full_html_with_elements(self):
		html_obj = HTML(False, False, False)
		test_element = html_element(False, "a", "Anchor")
		html_obj.add_element(test_element)
		html_obj.generate_html()
		self.assertEqual("<a>Anchor</a>\n", html_obj.html_string)
	
	def test_html_object_change_full_html(self):
		html_obj = HTML(True, True)
		html_obj.change_full_html()
		self.assertEqual(False, html_obj.is_full_html)
		
	def test_html_object_change_has_body(self):
		html_obj = HTML(True, True)
		html_obj.change_has_body()
		self.assertEqual(False, html_obj.has_body)