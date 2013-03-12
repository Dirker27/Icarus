import pygame

class Screen(object):
	def __init__(self, bckgdImg):
		pygame.init()

		self.background = pygame.image.load(bckgdImg)
		self.size       = (width, height) = self.background.get_size()

		self.screen     = pygame.display.set_mode(self.size)

		self.screen.blit(self.background, self.background.get_rect())

		pygame.display.flip()