from gameObject import GameObject
import math
import pygame

class PhysXObject(GameObject):

	def __init__(self, mass, pos, vel):
		GameObject.__init__(self, pos)

		self.mass = mass
		self.d_x  = vel[0]
		self.d_y  = vel[1]

		# initial image flips
		if (self.d_x < 0) :
			self.image = pygame.transform.flip(self.image, True, False)
		'''if (self.d_y < 0) :
			self.image = pygame.transform.flip(self.image, False, True)'''

	def momentum(self):
		return self.mass * math.sqrt( (self.d_x ** 2) + (self.d_y ** 2) )

	def update(self, time_elapsed):
		GameObject.update(self, time_elapsed)
		time_elapsed /= 1000.0

		self.pos.x += (self.d_x * time_elapsed)
		self.pos.y += (self.d_y * time_elapsed)