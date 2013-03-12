class Map(object):

	def __init__(self):
		self.bckgdImg = "../img/background/map01.jpg"

	def __str__(self):
		s = ""
		s += "Background: " + self.bckgdImg
		return s 
