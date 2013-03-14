import pygame

from objects import Sprite

class Button(Sprite):

	def __init__( self            ,
		          loc             ,
		          size            ,
		          action          ,
	              image_up_file   = "../img/btn/button.png"      ,
	              image_down_file = "../img/btn/button_down.png" ):
		# super
		Sprite.__init__(self, loc, size, image_up_file)

		# image data
		self.image_up   = pygame.transform.scale(pygame.image.load(image_up_file)  , size)
		self.image_down = pygame.transform.scale(pygame.image.load(image_down_file), size)

		# button action
		self.action     = action

		# verification vars
		self.phase1     = False
		self.phase2     = False

	def click(self):
		self.action()

	def mouse_over(self):
		self.image = self.image_down

	def mouse_out(self):
		self.image = self.image_up

	def update(self, time_elapsed, events):
		# super
		Sprite.update(self, time_elapsed, events)

		hover = False
		# hover images
		if self.hover():
			self.mouse_over()
			hover = True
		else:
			self.mouse_out()


		for event in events:
			if (event == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
				if hover:
					self.phase1 = True
				else:
					self.phase1 = False

			if (event == pygame.MOUSEBUTTONUP) and (event.button == 1):
				if hover:
					self.phase2 = True
				else:
					self.phase2 = False

		if (self.phase1) and (self.phase1 == self.phase2):
			self.click()
			self.phase1, self.phase2 = False