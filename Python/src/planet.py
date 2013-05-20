import pygame
import math

from physx import PhysX_Object

class Planet(PhysX_Object):

	def __init__(self, location, category = 2):
		PhysX_Object.__init__(self, location, (0, 0), (0, 0), 1e5, 1)

		source = "../img/planet_" + str(category) + ".png"
		self.image = pygame.image.load(source)

	def update(self, time_elapsed, events):
		PhysX_Object.update(self, time_elapsed, events)

	def gravitate(self, other):
		d_x = math.fabs(self.x_loc) - math.fabs(other.x_loc)
		d_y = math.fabs(self.y_loc) - math.fabs(other.y_loc)
		r = (d_x ** 2) + (d_y ** 2)

		G = 6.67e1

		acc = G * self.mass / (r ** 1)

		other.x_acc += acc * (d_x / r)
		other.y_acc += acc * (d_y / r)




