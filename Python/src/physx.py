import math

from objects import Game_Object

class PhysX_Object(Game_Object):

	def __init__( self             ,
	              loc = (0.0, 0.0) ,
	              vel = (0.0, 0.0) ,
	              acc = (0.0, 0.0) ,
	              mass = 1         ):	
		# super
		Game_Object.__init__(self, loc, vel)

		# mass
		self.mass  = mass

		# acceleration
		self.x_acc = acc[0]
		self.y_acc = acc[1]

	def momentum(self):
		return self.mass * math.sqrt( (self.d_x ** 2) + (self.d_y ** 2) )

	def update(self, time_elapsed, events):
		Game_Object.update(self, time_elapsed, events)

		time_elapsed /= 1000.0	#convert [ms] to [s]

		self.x_vel += (self.x_acc * time_elapsed)
		self.y_vel += (self.y_acc * time_elapsed)

