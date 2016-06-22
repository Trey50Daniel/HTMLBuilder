from HTML import HTML
from html_element import html_element
from Tkinter import *
import sys

root = Tk()


class Html_Builder(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.options_list = [
			"table",
			"tr",
			"td",
			"h1",
			"h2",
			"h3",
			"h4",
			"h5",
			"h6",
			"br",
			"span",
			"div",
			"a",
			"link",
			"nav",
			"title",
			"abbr",
			"address",
			"code",
			"em",
			"progress",
			"strong",
			"sub",
			"sup",
			"time",
			"u",
			"var",
			"samp",
			"small",
			"q",
			"mark",
			"s",
			"pre",
			"ins",
			"form",
			"input",
			"button",
			"fieldset",
			"legend",
			"label",
			"datalist",
			"option",
			"optgroup",
			"textarea",
			"keygen",
			"output",
			"select",
			"img",
			"map",
			"area",
			"canvas",
			"iframe",
			"figure",
			"figcaption",
			"audio",
			"source",
			"track",
			"video",
			"ul",
			"li",
			"ol",
			"dl",
			"dt",
			"dd",
			"menu",
			"menuitem",
			"caption",
			"thead",
			"tbody",
			"tfoot",
			"col",
			"colgroup",
			"style",
			"header",
			"footer",
			"main",
			"section",
			"article",
			"aside",
			"details",
			"dialog",
			"summary",
			"head",
			"meta",
			"base",
			"script",
			"noscript",
			"embed",
			"object",
			"param",
			"blockquote",
			"hr",
			"b",
			"bdi",
			"bdo",
			"dfn",
			"cite",
			"del",
			"q",
			"meter",
			"rp",
			"rt",
			"ruby"
		]
		self.options_list.sort()
		self.add_item = False
		self.nested = False
		self.delete_something = False
		self.meta = False
		self.temp_dict = {}
		self.order_number = 1
		self.html_object = HTML()
		self.CheckVar1 = IntVar()
		self.CheckVar2 = IntVar()
		self.C1 = Checkbutton(root, text = "Full HTML", variable = self.CheckVar1, \
					 command = self.html_full, onvalue = 1, offvalue = 0, height=4, \
					 width = 15)
		self.C2 = Checkbutton(root, text = "Has Body", variable = self.CheckVar2, \
					 command = self.html_has_body, onvalue = 1, offvalue = 0, height=4, \
					 width = 15)
		self.C1.pack()
		self.C2.pack()
		self.generate_button = Button(root, text='Generate HTML', command= self.make_file)
		self.generate_button.place(x=30, y=115)
		self.add_element_button = Button(root, text='Add Element', command = self.add_html_element)
		self.add_element_button.place(x=30, y=15)
		self.order_button = Button(root, text='Order Elements', command = self.order_html)
		self.order_button.place(x=30, y=75)
		self.delete_button = Button(root, text='Delete Element', command = self.delete_html)
		self.delete_button.place(x=30, y=45)
	
	def html_has_body(self):
		if(self.CheckVar2.get() == 1):
			self.html_object.has_body = True
		else:
			self.html_object.has_body = False
	
	def html_full(self):
		if(self.CheckVar1.get() == 1):
			self.html_object.is_full_html = True
		else:
			self.html_object.is_full_html = False

	def el_is_nested(self):
		if(self.check_is_nested.get() == 1):
			self.nested = True
		else:
			self.nested = False
	
	def make_file(self):
		self.html_object.generate_html()
		self.html_object.generate_file()
	
	def add_html_element(self):
		if(self.add_item == False and self.delete_something == False):
			self.option = StringVar()
			self.text_element = StringVar()
			self.option_list_pane = apply(OptionMenu, (root, self.option) + tuple(self.options_list))
			self.option.set(self.options_list[0])
			self.option_list_pane.place(x=20, y=200)
			self.add_button = Button(root, text='Add', width=7, command = self.add)
			self.add_button.place(x=175, y=450)
			self.text_element_box = Entry(root, textvariable=self.text_element)
			self.text_element_box.place(x=130, y=200)
			self.check_is_nested = IntVar()
			self.check_is_nested_button = Checkbutton(root, text = "Is Nested Element", variable = self.check_is_nested, \
						 command = self.el_is_nested, onvalue = 1, offvalue = 0, height=2, \
						 width = 14)
			self.check_is_nested_button.place(x=260, y=200)
			self.has_meta = IntVar()
			self.has_meta_button = Checkbutton(root, text = "Has Attributes", variable = self.has_meta, \
						 command = self.el_has_meta, onvalue = 1, offvalue = 0, height=2, \
						 width = 14)
			self.has_meta_button.place(x=260, y=275)
			self.add_item = True
		else:
			toplevel = Toplevel()
			label1 = Label(toplevel, text='Please finish your current action!', height=5, width=50)
			label1.pack()
	
	def el_has_meta(self):
		if(self.has_meta.get() == 1):
			self.meta = True
			self.meta_label = Label(root, text='Attribute Text:')
			self.meta_label.place(x=20, y=275)
			self.add_meta_button = Button(root, text='Add Attribute', width=11, command = self.add_meta)
			self.add_meta_button.place(x=115, y=330)
			self.value_label = Label(root, text='Attribute Value:')
			self.value_label.place(x=20, y=300)
			self.meta_text = StringVar()
			self.meta_element_box = Entry(root, textvariable=self.meta_text)
			self.meta_element_box.place(x=115, y=275)
			self.value_text = StringVar()
			self.value_box = Entry(root, textvariable=self.value_text)
			self.value_box.place(x=115, y=300)
		else:
			self.meta = False
	
	def add_meta(self):
		self.temp_dict[self.meta_text.get()] = self.value_text.get()
		print self.temp_dict[self.meta_text.get()]
		#self.html_object.meta_dict = self.temp_dict
	
	def order_html(self):
		square = self.html_object.is_full_html
		
	def delete_html(self):
		if not self.html_object.element_list:
			toplevel2 = Toplevel()
			label1 = Label(toplevel2, text='There are no items to delete', height=5, width=50)
			label1.pack()
		elif(self.add_item):
			toplevel3 = Toplevel()
			label1 = Label(toplevel3, text='Please finish your current action!', height=5, width=50)
			label1.pack()
		else:
			self.delete_something = True
			self.w = Spinbox(root, values=tuple(self.html_object.get_element_list()), width=30)
			self.w.place(x=175, y=225)
			self.delete_button = Button(root, text='Delete', width=7, command = self.delete)
			self.delete_button.place(x=175, y = 275)
		
	def delete(self):
		self.deleted_object = self.w.get()
		self.html_object.del_element(self.deleted_object)
		self.delete_something = False
		self.w.destroy()
		self.delete_button.destroy()
		
	def add(self):
		element_object = html_element(self.nested, self.option.get(), self.text_element.get(), self.order_number, self.temp_dict)
		temp = self.html_object.get_top_element_nested_level()
		if (element_object.is_nested):
			element_object.nested_level = temp + 1
			print element_object.nested_level
		else:
			temp = 0
			element_object.nested_level = 0
		self.html_object.add_element(element_object)
		self.order_number += 1
		
		#destroy all of the add options once the object has been added
		self.add_item = False
		self.nested = False
		self.option_list_pane.destroy()
		self.add_button.destroy()
		self.text_element_box.destroy()
		self.check_is_nested_button.destroy()
		self.has_meta_button.destroy()
		self.value_box.destroy()
		self.value_label.destroy()
		if (self.meta):
			self.meta = False
			self.meta_label.destroy()
			self.meta_element_box.destroy()
			self.add_meta_button.destroy()

if __name__ == '__main__':
	root.geometry("500x500+100+150")
	root.title("Build HTML")
	root.config(bg='dark gray')
	app = Html_Builder(master=root)
	app.mainloop()