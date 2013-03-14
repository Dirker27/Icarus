import math
import pygame

from physx import PhysX_Object

class Ship(PhysX_Object):

	def __init__(self):
		PhysX_Object.__init__(self, (0, 100), (0, 0), (0, 0), 10000)

		self.img_thrust_full = pygame.image.load("../img/toastercat_thrust_full.png")
		self.img_thrust_med  = pygame.image.load("../img/toastercat_thrust_med.png")
		self.img_thrust_low  = pygame.image.load("../img/toastercat_thrust_low.png")
		self.img_thrust_off  = pygame.image.load("../img/toastercat_thrust_off.png")

		self.image = self.img_thrust_off

	def update(self, time_elapsed, events):
		PhysX_Object.update(self, time_elapsed, events)

		# event handling
		for event in events:
			if (event.type == pygame.KEYDOWN):
				if event.key == pygame.K_UP:
					self.y_acc -= 10
				elif event.key == pygame.K_DOWN:
					self.y_acc += 10

				if event.key == pygame.K_LEFT:
					self.x_acc -= 10
				elif event.key == pygame.K_RIGHT:
					self.x_acc += 10

		# thruster image selection
		if (math.fabs(self.x_acc) <= 25):
			self.image = self.img_thrust_off
		elif (math.fabs(self.x_acc) <= 50):
			self.image = self.img_thrust_low
		elif (math.fabs(self.x_acc) <= 75):
			self.image = self.img_thrust_med
		else:
			self.image = self.img_thrust_full

		# image flipping
		if (self.x_acc < 0) :
			self.image = pygame.transform.flip(self.image, True, False)
