import pygame

from pygame.sprite import Sprite
from vec2d         import vec2d

class Game_Object(Sprite):

	def __init__( self                                       , 
		          loc        = (0.0, 0.0)                    ,
		          vel        = (0.0, 0.0)                    ,
		          size       = (50, 50)                      , 
		          image_file = "../img/ToasterCatSprite.png" ):
		# super
		Sprite.__init__(self)

		# location
		self.x_loc = float(loc[0])
		self.y_loc = float(loc[1])

		# velocity
		self.x_vel = float(vel[0])
		self.y_vel = float(vel[1])
		
		# image data
		self.image = pygame.image.load(image_file).convert_alpha()
		self.image = pygame.transform.scale(self.image, size)
		self.image_w, self.image_h = self.image.get_size()

		# initial image flips
		if (self.x_vel < 0) :
			self.image = pygame.transform.flip(self.image, True, False)
		'''if (self.d_y < 0) :
			self.image = pygame.transform.flip(self.image, False, True)'''


	def __lt__(self, other):
		return (self.x_loc < other.x_loc) and (self.y_loc < other.y_loc)

	def update(self, time_elapsed):
		time_elapsed /= 1000.0	#convert [ms] to [s]

		self.x_loc += (self.x_vel * time_elapsed)
		self.y_loc += (self.y_vel * time_elapsed)