import pygame
from random import choice, randint

from interface import User_Interface
from ship      import Ship
from planet    import Planet
class Game(User_Interface):

	def __init__(self):
		# super
		User_Interface.__init__(self, "../img/background/title.jpg") #, pygame.RESIZABLE)
		self.debug = True

		self.player = Ship()
		self.planets = []

		for i in range(3):
			x = randint(0, self.SCREEN_WIDTH)
			y = randint(0, self.SCREEN_HEIGHT)
			c = choice( (1, 2, 3) )
			self.planets.append( Planet((x, y), c) )
			self.object_list.append(self.planets[i])

		self.object_list.append(self.player)

	def execute(self):
		User_Interface.execute(self)

	def update(self):

		# Gravity emulation b/c MurrahWhynn is taking a while...
		for p in self.planets:
			p.gravitate(self.player)

		# SCREEN WALLS OF DETH!!!
		if (self.player.x_loc > self.SCREEN_WIDTH) or (self.player.x_loc < 0):
			self.cycle = False
		elif (self.player.y_loc > self.SCREEN_HEIGHT) or (self.player.y_loc < 0):
			self.cycle = False


	def repaint(self):
		User_Interface.repaint(self)

		font = pygame.font.Font(None, 20)

		text = "X-Thrust: " + str(self.player.x_thrust)
		self.screen.blit(font.render(text, True, (255,255,255)), (25, 25))

		text = "Y-Thrust: " + str(self.player.y_thrust)
		self.screen.blit(font.render(text, True, (255,255,255)), (25, 50))