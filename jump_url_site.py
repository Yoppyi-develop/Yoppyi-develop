import ui
import requests
import appex
import console
from google import google_url


class hub (object):
	def __init__(self):
		self.v = ui.load_view()
		self.v['button1'].action = self.google_jump
	def google_jump(self,sender):
		g = google_url()
		g.present_view()


h = hub()

h.v.present('sheet')
