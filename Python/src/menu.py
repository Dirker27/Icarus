import pygame
import sys
import math

from screen  import Screen
from physics import PhysXObject
from random  import choice, randint

class Menu(Screen):

	def __init__(self):
		Screen.__init__(self, "../img/background/title.jpg", pygame.NOFRAME)

		self.clock = pygame.time.Clock()

		self.run()

	def run(self):

		obj_list = []
		for i in range(0, 10):
			obj_list.append(
				 PhysXObject( 10                                                              , 
				              (randint(0, self.SCREEN_WIDTH), randint(0, self.SCREEN_HEIGHT)) ,
				              (randint(-100, 100)           , randint(-100, 100) )          ) )

		time_total = 0
		while True:
			self.screen.blit(self.background, self.background.get_rect())

			time_elapsed = self.clock.tick(60)
			time_total += time_elapsed

			for obj in obj_list:
				# restrict to bounds
				if (obj.pos.x > self.SCREEN_WIDTH):
					obj.d_x = -(math.fabs(obj.d_x))
					obj.image = pygame.transform.flip(obj.image, True, False)
				elif (obj.pos.x < 0):
					obj.d_x = math.fabs(obj.d_x)
					obj.image = pygame.transform.flip(obj.image, True, False)

				if (obj.pos.y > self.SCREEN_HEIGHT):
					obj.d_y = -(math.fabs(obj.d_y))
					#obj.image = pygame.transform.flip(obj.image, False, True)
				elif (obj.pos.y < 0):
					obj.d_y = math.fabs(obj.d_y)
					#obj.image = pygame.transform.flip(obj.image, False, True)

				# draw
				obj.update(time_elapsed)
				self.blit_obj(obj)

			pygame.display.flip()

			if (time_total >= 20e3):
				sys.exit()
