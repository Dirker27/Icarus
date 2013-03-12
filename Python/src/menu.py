import pygame
import sys

from screen import Screen

class Menu(Screen):
	def __init__(self):
		super(Menu, self).__init__("../img/background/title.jpg")

		self.clock = pygame.time.Clock()

		self.run()

	def run(self):
		time_passed = 0
		while True:
			time_passed += self.clock.tick(50)


			if (time_passed >= 2000):
				sys.exit()
