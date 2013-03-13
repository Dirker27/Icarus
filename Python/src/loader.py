import pickle, shelve
import pygame

from screen import Screen

class Loader(Screen):

	def __init__(self):
		Screen.__init__(self, "../img/background/load.jpg", pygame.NOFRAME, (400, 300))

	def do_a_thing():
		tasklist = []
		tasklist.append( ["Planets", self.load_planets] )
		tasklist.append( ["Ships"  , self.load_ships] )

		current_task = 0
		task_length = len(tasklist)
		run = True
		while run:
			self.screen.blit(self.background, self.background.get_rect())

			if (current_task == task_length):
				run = False
			else:
				myfont = pygame.font.SysFont("monospace", 15)
				label = myfont.render(tasklist[current_task][0], 1, (255,255,0))
				screen.blit(label, (100, 100))

				pygame.display.flip()

				tasklist[current_task][1]()
				current_task += 1

			pygame.display.update()

		pygame.quit()

	def load_planets():
		atom_data = shelve.open("../dat/planet_data.dat")
		atom_data["Hydrogen"]   = ["Hydrogen"  , "H" , './images/hydrogen.png'  , 1 ]
		atom_data["Helium"]     = ["Helium"    , "He", './images/helium.png'    , 2 ]
		atom_data["Lithium"]    = ["Lithium"   , "Li", './images/lithium.png'   , 3 ]
		atom_data["Beryllium"]  = ["Beryllium" , "Be", './images/beryllium.png' , 4 ]
		atom_data["Boron"]      = ["Boron"     , "B" , './images/boron.png'     , 5 ]
		atom_data["Carbon"]     = ["Carbon"    , "C" , './images/carbon.png'    , 6 ]
		atom_data["Nitrogen"]   = ["Nitrogen"  , "N" , './images/nitrogen.png'  , 7 ]
		atom_data["Oxygen"]     = ["Oxygen"    , "O" , './images/oxygen.png'    , 8 ]
		atom_data["Fluorine"]   = ["Fluorine"  , "F" , './images/fluorine.png'  , 9 ]
		atom_data["Neon"]       = ["Neon"      , "Ne", './images/neon.png'      , 10]
		atom_data["Sodium"]     = ["Sodium"    , "Na", './images/sodium.png'    , 11]
		atom_data["Magnesium"]  = ["Magnesium" , "Mg", './images/magnesium.png' , 12]
		atom_data["Aluminum"]   = ["Aluminum"  , "Al", './images/aluminum.png'  , 13]
		atom_data["Silicon"]    = ["Silicon"   , "Si", './images/silicon.png'   , 14]
		atom_data["Phosphorus"] = ["Phosphorus", "P" , './images/phosphorus.png', 15]
		atom_data["Sulfur"]     = ["Sulfur"    , "S" , './images/sulfur.png'    , 16]
		atom_data["Chlorine"]   = ["Chlorine"  , "Cl", './images/chlorine.png'  , 17]
		atom_data["Argon"]      = ["Argon"     , "Ar", './images/argon.png'     , 18]
		atom_data["Potassium"]  = ["Potassium" , "K" , './images/potassium.png' , 19]
		atom_data["Calcium"]    = ["Calcium"   , "Ca", './images/calcium.png'   , 20]
		atom_data["Titanium"]   = ["Titanium"  , "Ti", './images/titanium.png'  , 22]
		atom_data["Iron"]       = ["Iron"      , "Fe", './images/iron.png'      , 26]
		atom_data["Nickel"]     = ["Nickel"    , "Ni", './images/nickel.png'    , 28]
		atom_data["Copper"]     = ["Copper"    , "Cu", './images/copper.png'    , 29]
		atom_data["Zinc"]       = ["Zinc"      , "Zn", './images/nickel.png'    , 30]    
		atom_data["Bromine"]    = ["Bromine"   , "Br", './images/bromine.png'   , 35]
		atom_data["Silver"]     = ["Silver"    , "Ag", './images/silver.png'    , 47]
		atom_data["Iodine"]     = ["Iodine"    , "I" , './images/iodine.png'    , 53]
		atom_data["Gold"]       = ["Gold"      , "Au", './images/gold.png'      , 79]
	    
	    # insert
		atom_data.sync()
		atom_data.close()

		print("planets loaded!\n")

	def load_ships():
		atom_data = shelve.open("../dat/ship_data.dat")
		atom_data["Hydrogen"]   = ["Hydrogen"  , "H" , './images/hydrogen.png'  , 1 ]
		atom_data["Helium"]     = ["Helium"    , "He", './images/helium.png'    , 2 ]
		atom_data["Lithium"]    = ["Lithium"   , "Li", './images/lithium.png'   , 3 ]
		atom_data["Beryllium"]  = ["Beryllium" , "Be", './images/beryllium.png' , 4 ]
		atom_data["Boron"]      = ["Boron"     , "B" , './images/boron.png'     , 5 ]
		atom_data["Carbon"]     = ["Carbon"    , "C" , './images/carbon.png'    , 6 ]
		atom_data["Nitrogen"]   = ["Nitrogen"  , "N" , './images/nitrogen.png'  , 7 ]
		atom_data["Oxygen"]     = ["Oxygen"    , "O" , './images/oxygen.png'    , 8 ]
		atom_data["Fluorine"]   = ["Fluorine"  , "F" , './images/fluorine.png'  , 9 ]
		atom_data["Neon"]       = ["Neon"      , "Ne", './images/neon.png'      , 10]
		atom_data["Sodium"]     = ["Sodium"    , "Na", './images/sodium.png'    , 11]
		atom_data["Magnesium"]  = ["Magnesium" , "Mg", './images/magnesium.png' , 12]
		atom_data["Aluminum"]   = ["Aluminum"  , "Al", './images/aluminum.png'  , 13]
		atom_data["Silicon"]    = ["Silicon"   , "Si", './images/silicon.png'   , 14]
		atom_data["Phosphorus"] = ["Phosphorus", "P" , './images/phosphorus.png', 15]
		atom_data["Sulfur"]     = ["Sulfur"    , "S" , './images/sulfur.png'    , 16]
		atom_data["Chlorine"]   = ["Chlorine"  , "Cl", './images/chlorine.png'  , 17]
		atom_data["Argon"]      = ["Argon"     , "Ar", './images/argon.png'     , 18]
		atom_data["Potassium"]  = ["Potassium" , "K" , './images/potassium.png' , 19]
		atom_data["Calcium"]    = ["Calcium"   , "Ca", './images/calcium.png'   , 20]
		atom_data["Titanium"]   = ["Titanium"  , "Ti", './images/titanium.png'  , 22]
		atom_data["Iron"]       = ["Iron"      , "Fe", './images/iron.png'      , 26]
		atom_data["Nickel"]     = ["Nickel"    , "Ni", './images/nickel.png'    , 28]
		atom_data["Copper"]     = ["Copper"    , "Cu", './images/copper.png'    , 29]
		atom_data["Zinc"]       = ["Zinc"      , "Zn", './images/nickel.png'    , 30]    
		atom_data["Bromine"]    = ["Bromine"   , "Br", './images/bromine.png'   , 35]
		atom_data["Silver"]     = ["Silver"    , "Ag", './images/silver.png'    , 47]
		atom_data["Iodine"]     = ["Iodine"    , "I" , './images/iodine.png'    , 53]
		atom_data["Gold"]       = ["Gold"      , "Au", './images/gold.png'      , 79]
	    
	    # insert
		atom_data.sync()
		atom_data.close()

		print("ships loaded!\n")