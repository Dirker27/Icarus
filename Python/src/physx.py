import math

from objects import Game_Object

class PhysX_Object(Game_Object):

	def __init__( self             ,
	              loc = (0.0, 0.0) ,
	              vel = (0.0, 0.0) ,
	              acc = (0.0, 0.0) ,
	              mass = 1         ,
	              spin = 0		   ):	
		# super
		Game_Object.__init__(self, loc, vel)

		# mass
		self.mass  = mass

		#spin 
		self.spin = spin

		# acceleration
		self.x_acc = acc[0]
		self.y_acc = acc[1]

		# gravity
		self.GRAVITY = 10 * (6.67e-11)

	def update(self, time_elapsed, events):
		Game_Object.update(self, time_elapsed, events)

		time_elapsed /= 1000.0	#convert [ms] to [s]

		self.x_vel += (self.x_acc * time_elapsed)
		self.y_vel += (self.y_acc * time_elapsed)

	def x_momentum(self):
		return self.mass * x_vel

	def y_momentum(self):
		return self.mass * y_vel

	def x_kinetic_energy(self):
		return .5 * self.mass * (self.x_vel**2)

	def y_kinetic_energy(self):
		return .5 * self.mass * (self.y_vel**2)
