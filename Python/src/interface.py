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

		# UI contents
		self.object_list = []

		# UI time
		self.clock      = pygame.time.Clock()
		self.time_total = 0

		self.cycle = True

	def blit_obj(self, obj):
		draw_pos = obj.image.get_rect().move( obj.x_loc - (obj.image_w/2) ,
                                              obj.y_loc - (obj.image_h/2) )
		self.screen.blit(obj.image, draw_pos)

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

			for event in pygame.event.get():
				if event == pygame.QUIT:
					self.cycle = False
					break

				for obj in self.object_list:
					obj.event_handling(event)


			'''if pygame.MOUSEBUTTONDOWN in events:
				self.run = False'''

			# initial render
			self.screen.blit(self.bckgd, self.bckgd.get_rect())

			# content event handling / rendering
			for obj in self.object_list:
				obj.timed_update(time_elapsed)
				self.blit_obj(obj)

			# version-specific data
			self.update()

			pygame.display.flip()
			pygame.display.update()

		self.cycle = True
		self.end_UI()
