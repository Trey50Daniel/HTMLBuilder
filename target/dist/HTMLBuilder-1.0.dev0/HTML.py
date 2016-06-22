import os

class HTML():
	def __init__(self, full_html=False, body=False, head=False):
		self.is_full_html = full_html
		self.has_body = body
		self.has_head = head
		self.element_list = []
		self.html_string = ""
		self.inc_id = 0
		
	def __str__(self):
		return self.html_string
		

	def get_element_list(self):
		return self.element_list
		
	def get_element(self, index):
		return self.element_list[index]
	
	def get_top_element_nested_level(self):
		if not self.element_list:
			return 0
		else:
			return self.element_list[len(self.element_list) - 1].nested_level
		
	def set_element_nested_level(self, index, level):
		self.element_list[index].nested_level = level
	
	def set_element(self, index, object):
		temp = self.element_list[index]
		self.element_list[index] = object
	
	def change_full_html(self):
		if(self.is_full_html):
			self.is_full_html = False
		else:
			self.is_full_html = True
	
	def change_has_body(self):
		if(self.has_body):
			self.has_body = False
		else:
			self.has_body = True
	
	#A function to generate html based upon the elements added to the list
	def generate_html(self):
		if(self.is_full_html):
			self.html_string += "<!DOCTYPE html>\n <html>\n"
			if(self.has_head):
				self.html_string += "<head>\n</head>\n"
			if(self.has_body):
				self.html_string += "<body>\n"
				if not self.element_list:
					self.html_string += "</body>\n"
					self.html_string += "</html>"
				else:
					for element in self.element_list:
						self.html_string += element.__str__()
					self.html_string += "</body>\n"
					self.html_string += "</html>"
			else:
				if not self.element_list:
					self.html_string += "</html>"
				else:
					for element in self.element_list:
						self.html_string += element.__str__()
					self.html_string += "</html>"
		else:
			if not self.element_list:
				self.html_string = ""
			else:
				for element in self.element_list:
					self.html_string += element.__str__()
	
	def add_element(self, object):
		object.id = self.inc_id
		self.element_list.append(object)
		self.inc_id += 1
	
	def order_elements(self, ordered_list):
		self.element_list = ordered_list
	
	def del_element(self, object):
		index = self.element_list.index(object)
		#print self.element_list[index]
		del self.element_list[index]
	
	def generate_file(self):
		if(os.path.isdir("generatedHTML")):
			os.chdir("generatedHTML")
			os.remove("generated.html")
			os.chdir("..")
			os.rmdir("generatedHTML")
		os.mkdir("generatedHTML")
		os.chdir("generatedHTML")

		output_html = open("generated.html", "w")

		output_html.write(self.html_string)
		output_html.close()
