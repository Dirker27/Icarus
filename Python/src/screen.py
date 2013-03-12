import pygame

class Screen(object):

	def __init__(self, bckgdImg, mode = pygame.RESIZABLE):
		# pygame inits
		pygame.init()
		pygame.display.init()
		
		# calibrate size to 75% scale OS's logged screen resolution
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.list_modes(32)[0]
		self.SCREEN_WIDTH  *= 0.75
		self.SCREEN_HEIGHT *= 0.75
		self.size = (int(self.SCREEN_WIDTH), int(self.SCREEN_HEIGHT))

		# load background
		self.background = pygame.transform.scale(pygame.image.load(bckgdImg), self.size)

		# construct surface object
		self.screen = pygame.display.set_mode(self.size, mode)

		# initial blit
		self.screen.blit(self.background, self.background.get_rect())
		pygame.display.flip()


	def blit_obj(self, obj):
		draw_pos = obj.image.get_rect().move( obj.pos.x - (obj.image_w/2) ,
                                              obj.pos.y - (obj.image_h/2) )
		self.screen.blit(obj.image, draw_pos)