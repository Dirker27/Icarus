import pygame
import math

class Sprite(object):

	def __init__( self              , 
		          loc  = (0.0, 0.0) ,
		          size = (50, 50)   ,
		          image_file = "../img/toastercat_raw.png"):
		# positional data
		self.x_loc = float(loc[0])
		self.y_loc = float(loc[1])

		# image data
		self.image = pygame.image.load(image_file)
		self.image = pygame.transform.scale(self.image, size)
		self.image_w, self.image_h = self.image.get_size()

	def update(self, time_elapsed, events):
		self.x_loc = self.x_loc

	def hover(self):
		return (self.get_rect().collidepoint(pygame.mouse.get_pos()) == True)

	def get_rect(self):
		return self.image.get_rect().move( self.x_loc - (self.image_w/2) ,
                                           self.y_loc - (self.image_h/2) )



class Game_Object(Sprite):

	def __init__( self                                       , 
		          loc        = (0.0, 0.0)                    ,
		          vel        = (0.0, 0.0)                    ,
		          size       = (50, 50)                      , 
		          image_file = "../img/ToasterCatSprite.png" ):
		# super
		Sprite.__init__(self, loc, size, image_file)

		# velocity
		self.x_vel = float(vel[0])
		self.y_vel = float(vel[1])
		
	def __lt__(self, other):
		return (self.x_loc < other.x_loc) and (self.y_loc < other.y_loc)

	def update(self, time_elapsed, events):
		time_elapsed /= 1000.0	#convert [ms] to [s]

		self.x_loc += (self.x_vel * time_elapsed)
		self.y_loc += (self.y_vel * time_elapsed)