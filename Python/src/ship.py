import math
import pygame

from physx import PhysX_Object

class Ship(PhysX_Object):

	def __init__(self):
		PhysX_Object.__init__(self, (0, 100), (0, 0), (0, 0), (50, 50), 2.2e3)

		self.img_thrust_full = pygame.image.load("../img/toastercat_thrust_full.png")
		self.img_thrust_med  = pygame.image.load("../img/toastercat_thrust_med.png")
		self.img_thrust_low  = pygame.image.load("../img/toastercat_thrust_low.png")
		self.img_thrust_off  = pygame.image.load("../img/toastercat_thrust_off.png")

		self.image = self.img_thrust_off

		# control attributes
		self.x_thrust = 0
		self.y_thrust = 0
		self.thrust_mode = True
		self.thrust_max  = 10
		self.inert_damp  = 0.25


	def update(self, time_elapsed, events):
		PhysX_Object.update(self, time_elapsed, events)

		# event handling
		for event in events:

			if (event.type == pygame.KEYDOWN):

				# SPACE == change thruster mode
				if event.key == pygame.K_SPACE:
					self.thrust_mode = False

				# UP/DOWN == vertical thrusters
				if event.key == pygame.K_UP:
					if self.thrust_mode:
						self.y_thrust -= 1
					else:
						self.y_vel -= 15
				elif event.key == pygame.K_DOWN:
					if self.thrust_mode:
						self.y_thrust += 1
					else:
						self.y_vel += 15

				# LEFT/RIGHT = horizontal thrusters
				if event.key == pygame.K_LEFT:
					if self.thrust_mode:
						self.x_thrust -= 1
					else:
						self.x_vel -= 15
				elif event.key == pygame.K_RIGHT:
					if self.thrust_mode:
						self.x_thrust += 1
					else:
						self.x_vel += 15

		# thruster image selection
		if (math.fabs(self.x_thrust) <= 1):
			self.load_image(self.img_thrust_off)
		elif (math.fabs(self.x_thrust) <= 3):
			self.load_image(self.img_thrust_low)
		elif (math.fabs(self.x_thrust) <= 5):
			self.load_image(self.img_thrust_med)
		else:
			self.image = self.img_thrust_full

		# image flipping
		if (self.x_thrust < 0) :
			self.image = pygame.transform.flip(self.image, True, False)

		# thrust implementation
		#self.x_acc += self.x_thrust * (time_elapsed / 1000)
		#self.y_acc += self.y_thrust * (time_elapsed / 1000)

		self.x_acc = self.x_thrust * 5
		self.y_acc = self.y_thrust * 5

		# inertial dampening
		self.x_vel -= (self.x_vel * self.inert_damp) * (time_elapsed / 1000)
		self.y_vel -= (self.y_vel * self.inert_damp) * (time_elapsed / 1000)
