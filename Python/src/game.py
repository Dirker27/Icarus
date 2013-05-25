import pygame
from random import choice, randint

from interface import User_Interface
from ship      import Ship
from planet    import Planet
class Game(User_Interface):

	def __init__(self):
		# super
		User_Interface.__init__(self, "../img/background/title.jpg") #, pygame.RESIZABLE)
		self.debug = True

		self.player = Ship()
		self.planets = []

		for i in range(3):
			x = randint(0, self.SCREEN_WIDTH)
			y = randint(0, self.SCREEN_HEIGHT)
			c = choice( (1, 2, 3) )
			self.planets.append( Planet((x, y), c) )
			self.object_list.append(self.planets[i])

		self.object_list.append(self.player)

	def execute(self):
		User_Interface.execute(self)

	def update(self):

		# Gravity emulation b/c MurrahWhynn is taking a while...
		for p in self.planets:
			p.gravitate(self.player)

		# SCREEN WALLS OF DETH!!!
		if (self.player.x_loc > self.SCREEN_WIDTH) or (self.player.x_loc < 0):
			self.cycle = False
		elif (self.player.y_loc > self.SCREEN_HEIGHT) or (self.player.y_loc < 0):
			self.cycle = False


	def repaint(self):
		User_Interface.repaint(self)

		font = pygame.font.Font(None, 20)

		if (self.debug):
			text = "Thr: (" + str(int(self.player.x_thrust)) + ", " + str(int(self.player.y_thrust)) + ")"
			self.screen.blit(font.render(text, True, (255,255,255)), (25, 25))

			text = "Acc: (" + str(int(self.player.x_acc)) + ", " + str(int(self.player.y_acc)) + ")"
			self.screen.blit(font.render(text, True, (255,255,255)), (25, 50))

			text = "Vel: (" + str(int(self.player.x_vel)) + ", " + str(int(self.player.y_vel)) + ")"
			self.screen.blit(font.render(text, True, (255,255,255)), (25, 75))


	def blit_obj(self, obj):
		if (obj != self.player):
			draw_pos = obj.get_rect()

			if (self.debug):
				# background
				t_pos = (obj.x_loc - 200, obj.y_loc - 200)
				backgrd = pygame.Surface( (400, 400) )
				backgrd.fill( (255, 255, 0) )
				backgrd.set_alpha(50)
				self.screen.blit(backgrd, t_pos)
				#color = (255, 255, 0)
				#pos = (int(obj.x_loc), int(obj.y_loc))
				#pygame.draw.circle(self.screen, color, pos, 400)

			self.screen.blit(obj.image, draw_pos)

			if (self.debug):
				#TL
				point = pygame.Surface( (4, 4) )
				point.fill( (0, 255, 0) )
				point.set_alpha(75)
				self.screen.blit(point, t_pos)

				#core
				t_pos = (obj.x_loc-2, obj.y_loc-2)
				point.fill( (255, 0, 0) )
				point.set_alpha(100)
				self.screen.blit(point, t_pos)
		else:
			User_Interface.blit_obj(self, obj)