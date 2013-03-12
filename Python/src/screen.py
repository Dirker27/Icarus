import pygame

class Screen(object):
	def __init__(self, bckgdImg):
		# pygame inits
		pygame.init()
		pygame.display.init()

		# load background
		self.background = pygame.image.load(bckgdImg)
		
		# calibrate size to 75% scale OS's logged screen resolution
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.list_modes(32)[0]
		self.SCREEN_WIDTH  *= 0.75
		self.SCREEN_HEIGHT *= 0.75
		self.size = (int(self.SCREEN_WIDTH), int(self.SCREEN_HEIGHT))

		# construct surface object
		self.screen = pygame.display.set_mode(self.size)

		# initial blit
		self.screen.blit(self.background, self.background.get_rect())
		pygame.display.flip()