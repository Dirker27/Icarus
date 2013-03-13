from loader import Loader
from menu   import Menu

class World(object):

	def __init__(self):
		# Dump to data files
		self.loader = Loader()
		self.menu   = Menu()


	def execute(self):
		self.loader.initial_load()
		self.menu.run()