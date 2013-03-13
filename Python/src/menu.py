# Python libraries
import pygame
import os, sys
import math
from random import choice, randint

# Icarus libraries
from interface import User_Interface
from physx     import PhysX_Object

class Menu(User_Interface):

	def __init__(self):
		User_Interface.__init__(self, "../img/background/title.jpg", pygame.RESIZABLE)
		self.clock = pygame.time.Clock()

	def run(self):
		self.startUI()

		obj_list = []
		for i in range(0, 15):
			obj_list.append(
				 PhysX_Object( (randint(0, self.SCREEN_WIDTH), randint(0, self.SCREEN_HEIGHT)) ,
				               (randint(-100, 100)           , randint(-100, 100))           ) )

		speedup   = False
		speeddown = False
		printout  = False

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
					elif event.key == pygame.K_p:
						printout = True

			self.screen.blit(self.background, self.background.get_rect())

			for obj in obj_list:
				# restrict to bounds
				if (obj.x_loc > self.SCREEN_WIDTH):
					obj.x_vel = -(math.fabs(obj.x_vel))
					obj.image = pygame.transform.flip(obj.image, True, False)
				elif (obj.x_loc < 0):
					obj.x_vel = math.fabs(obj.x_vel)
					obj.image = pygame.transform.flip(obj.image, True, False)

				if (obj.y_loc > self.SCREEN_HEIGHT):
					obj.y_vel = -(math.fabs(obj.y_vel))
					#obj.image = pygame.transform.flip(obj.image, False, True)
				elif (obj.y_loc < 0):
					obj.y_vel = math.fabs(obj.y_vel)
					#obj.image = pygame.transform.flip(obj.image, False, True)

				# speedup if necessary
				if speedup:
					obj.x_vel *= 1.25
					obj.y_vel *= 1.25
				elif speeddown:
					obj.x_vel *= 0.75
					obj.y_vel *= 0.75

				if printout:
					print("[", obj.x_loc, ", ", obj.y_loc, "]")
					print("(", obj.x_vel, ", ", obj.y_vel, ")")
					print("<", obj.x_acc, ", ", obj.y_acc, ">")



				# draw
				obj.update(time_elapsed)
				self.blit_obj(obj)

			pygame.display.flip()
			pygame.display.update()

			speedup   = False
			speeddown = False
			printout  = False

		self.endUI()
