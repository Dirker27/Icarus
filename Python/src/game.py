import pygame

from interface import User_Interface
from ship      import Ship
class Game(User_Interface):

	def __init__(self):
		# super
		User_Interface.__init__(self, "../img/background/title.jpg", pygame.NOFRAME)
		self.player = Ship()

		self.object_list.append(self.player)

	def execute(self):
		User_Interface.execute(self)

	def update(self):
		if (self.player.x_loc > self.SCREEN_WIDTH) or (self.player.x_loc < 0):
			self.cycle = False