import pygame

class User_Interface(object):

	def __init__(self, bckgdImg, mode = pygame.RESIZABLE, size = None):
		# pygame inits
		pygame.init()
		pygame.display.init()

		# callibrate sizing elements
		if (size != None):
			self.SCREEN_WIDTH  = size[0]
			self.SCREEN_HEIGHT = size[1]
		else:	
			# calibrate size to 75% scale OS's logged screen resolution
			self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.list_modes(32)[0]
			self.SCREEN_WIDTH  *= 0.75
			self.SCREEN_HEIGHT *= 0.75

		# UI characteristics
		self.size = (int(self.SCREEN_WIDTH), int(self.SCREEN_HEIGHT))
		self.mode = mode

		# load background
		self.background = pygame.transform.scale(pygame.image.load(bckgdImg), self.size)

		# surface object to be null until activation
		self.screen = None


	def blit_obj(self, obj):
		draw_pos = obj.image.get_rect().move( obj.x_loc - (obj.image_w/2) ,
                                              obj.y_loc - (obj.image_h/2) )
		self.screen.blit(obj.image, draw_pos)

	def startUI(self):
		# generate surface object/render window
		self.screen = pygame.display.set_mode(self.size, self.mode)

		# initial blit
		self.screen.blit(self.background, self.background.get_rect())
		pygame.display.flip()

	def endUI(self):
		pygame.quit()
