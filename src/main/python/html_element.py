class html_element():
	def __init__(self, el_is_nested=False, el=None, el_text=None, my_id=0, my_dict={}):
		self.is_nested = el_is_nested
		self.element = el
		self.nested_level = 0
		self.text = el_text
		self.element_string = ""
		self.id = my_id
		self.meta_dict = my_dict
		
	def __str__(self):
		if self.element == None:
			return ""
		#print self.meta_dict
		if not self.meta_dict:
			if(self.is_nested):
				for i in range(self.nested_level):
					self.element_string += "\t"
			self.element_string += "<" + self.element + ">" + self.text + "</" + self.element + ">\n"
		else:
			if(self.is_nested):
				for i in range(self.nested_level):
					self.element_string += "\t"
				
				self.element_string += "<" + self.element
				for key, value in self.meta_dict.iteritems():
					self.element_string += " " + key + "='" + value + "'"
					print self.element_string
				self.element_string += ">" + self.text + "</" + self.element + ">\n"
			else:
				self.element_string += "<" + self.element
				for key, value in self.meta_dict.iteritems():
					self.element_string += " " + key + "='" + value + "'"
				self.element_string += ">" + self.text + "</" + self.element + ">\n"
		return self.element_string