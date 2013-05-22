import pygame

class User_Interface(object):

	def __init__(self, bckgdImg, mode = pygame.NOFRAME, size = None):
		# pygame inits
		pygame.init()
		pygame.display.init()

		# calibrate sizing elements
		if (size != None):
			self.SCREEN_WIDTH  = size[0]
			self.SCREEN_HEIGHT = size[1]
		else:	
			# calibrate size to 75% scale OS's logged screen resolution
			self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.list_modes(32)[0]
			self.SCREEN_WIDTH  *= 0.75
			self.SCREEN_HEIGHT *= 0.75

		# UI characteristics
		self.size   = (int(self.SCREEN_WIDTH), int(self.SCREEN_HEIGHT))
		self.mode   = mode
		self.bckgd  = pygame.transform.scale(pygame.image.load(bckgdImg), self.size)
		self.screen = None
		self.debug  = False

		# UI contents
		self.object_list = []

		# UI time
		self.clock      = pygame.time.Clock()
		self.time_total = 0

		self.cycle = True

	def start_UI(self):
		# generate surface object/render window
		self.screen = pygame.display.set_mode(self.size, self.mode)

		# initial blit
		self.screen.blit(self.bckgd, self.bckgd.get_rect())
		pygame.display.flip()

	def end_UI(self):
		pygame.quit()

	def execute(self):
		self.start_UI()

		while self.cycle:
			# Time Tracking
			time_elapsed      = self.clock.tick(120)
			self.time_total  += time_elapsed

			events = []
			for event in pygame.event.get():
				if event == pygame.QUIT:
					self.cycle = False
					break

				events.append(event)

			# content event handling
			for obj in self.object_list:
				obj.update(time_elapsed, events)

			# version-specific data
			self.update()

			self.repaint()
			pygame.display.flip()
			pygame.display.update()

		self.cycle = True
		self.end_UI()

	def repaint(self):
		# initial render
		self.screen.blit(self.bckgd, self.bckgd.get_rect())

		# content rendering
		for obj in self.object_list:
			self.blit_obj(obj)

	def blit_obj(self, obj):
		draw_pos = obj.get_rect()

		if (self.debug):
			# background
			t_pos = (draw_pos[0], draw_pos[1])
			backgrd = pygame.Surface( (obj.image_w, obj.image_h) )
			backgrd.fill( (0, 0, 255) )
			backgrd.set_alpha(50)
			self.screen.blit(backgrd, t_pos)

		self.screen.blit(obj.image, draw_pos)

		if (self.debug):
			#TL
			point = pygame.Surface( (4, 4) )
			point.fill( (0, 255, 0) )
			point.set_alpha(75)
			self.screen.blit(point, t_pos)

			#core
			t_pos = (obj.x_loc-2, obj.y_loc-2)
			point.fill( (255, 0, 0) )
			point.set_alpha(100)
			self.screen.blit(point, t_pos)