import ui
import requests
import appex

class google_url (object):
	global v
	def __init__(self):
		self.v = ui.load_view()
		wb = self.v['webview1']
		wb.load_url('https://google.com')
		wb.bring_to_front()
	def present_view(self):
		self.v.present('sheet')
	def __main__(self):
		wb = v['webview1']
		wb.load_url('https://google.com')
		wb.bring_to_front()

