# Python libraries
import pygame
import os, sys
import math
from random import choice, randint

# Icarus libraries
from interface import User_Interface
from physx     import PhysX_Object
from button    import Button

class Main_Menu(User_Interface):

	def __init__(self):
		User_Interface.__init__(self, "../img/background/title.jpg", pygame.NOFRAME)

		self.object_list = self.get_critters(15)
		game_btn = Button((100,100), (150, 75), self.game_btn_action)
		self.object_list.append(game_btn)

		self.choice = None

	def get_critters(self, pop):
		obj_list = []
		for i in range(0, pop):
			obj_list.append(
				 PhysX_Object( (randint(0, self.SCREEN_WIDTH), randint(0, self.SCREEN_HEIGHT)) ,
				               (randint(-100, 100)           , randint(-100, 100)           )  ) )

		return obj_list

	def game_btn_action(self):
		self.cycle = False
		self.choice = 1

	def update(self):
		for obj in self.object_list:
			# restrict to bounds
			if (obj.x_loc > self.SCREEN_WIDTH):
				obj.x_vel = -(math.fabs(obj.x_vel))
			elif (obj.x_loc < 0):
				obj.x_vel = math.fabs(obj.x_vel)

			if (obj.y_loc > self.SCREEN_HEIGHT):
				obj.y_vel = -(math.fabs(obj.y_vel))
			elif (obj.y_loc < 0):
				obj.y_vel = math.fabs(obj.y_vel)

	def execute(self):
		User_Interface.execute(self)

		return self.choice