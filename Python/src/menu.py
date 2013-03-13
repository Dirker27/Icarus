import pygame
import os, sys
import math

from screen  import Screen
from physics import PhysXObject
from random  import choice, randint

class Menu(Screen):

	def __init__(self):
		Screen.__init__(self, "../img/background/title.jpg", pygame.RESIZABLE)

		self.clock = pygame.time.Clock()

		self.run()

	def run(self):
		obj_list = []
		for i in range(0, 15):
			obj_list.append(
				 PhysXObject( 10                                                              , 
				              (randint(0, self.SCREEN_WIDTH), randint(0, self.SCREEN_HEIGHT)) ,
				              (float(randint(-100, 100))    , float(randint(-100, 100)) )          ) )

		speedup = False
		speeddown = False

		run = True
		time_total = 0
		while True:
			time_elapsed = self.clock.tick(60)
			time_total += time_elapsed

			# Event handling/monitoring
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					break
				if (event.type == pygame.KEYDOWN):
					if event.key == pygame.K_UP:
						speedup = True
					elif event.key == pygame.K_DOWN:
						speeddown = True

			self.screen.blit(self.background, self.background.get_rect())

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

				# speedup if necessary
				if speedup:
					obj.d_x *= 1.25
					obj.d_y *= 1.25
				elif speeddown:
					obj.d_x *= 0.75
					obj.d_y *= 0.75

				# draw
				obj.update(time_elapsed)
				self.blit_obj(obj)

			pygame.display.flip()
			pygame.display.update()

			speedup = False
			speeddown = False

		pygame.quit()
