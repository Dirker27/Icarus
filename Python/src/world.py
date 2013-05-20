from loader import Loader
from menu   import Main_Menu
from game   import Game

class World(object):

	def __init__(self):
		# Dump to data files
		#self.loader = Loader()
		self.menu   = Main_Menu()

	def execute(self):
		#self.loader.initial_load()
		action = 1
		while (action != None):
			action = self.menu.execute()

			if (action == 1):
				g = Game()
				g.execute()
			elif (action == 0):
				exit()