class Map(object):

	def __init__(self):
		self.bckgdImg = "../images/bckgdImg1.png"

	def __str__(self):
		s = ""
		s += "Background: " + self.bckgdImg
		return s 
