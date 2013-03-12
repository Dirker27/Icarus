import pygame

from pygame.sprite import Sprite
from vec2d         import vec2d

class GameObject(Sprite):

	def __init__( self                                       , 
		          pos        = (0, 0)                        ,
		          size       = (50, 50)                      , 
		          image_file = "../img/ToasterCatSprite.png" ):
		# super
		Sprite.__init__(self)

		# positional data
		self.pos = vec2d(pos)
		
		# image data
		self.image = pygame.image.load(image_file) #.convert_alpha()
		self.image = pygame.transform.scale(self.image, size)
		self.image_w, self.image_h = self.image.get_size()


	def __lt__(self, other):
		return (self.pos.x < other.pos.x) and (self.pos.y < other.pos.y)

	def update(self, time_elapsed):
		self.pos = self.pos