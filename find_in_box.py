# This module is depricated by lib/windows
import pyautogui, readbox
from pyclick import HumanClicker
from random import randint

class FindItem:
	def __init__(self, title_img):
		self.__title_img = title_img
		self.move = HumanClicker()


	def get_box_dimention(self):
		if pyautogui.locateOnScreen(self.__title_img):
			box_dimention = pyautogui.locateOnScreen(self.__title_img)
			x = box_dimention[0] + 10
			x2 = x + 119
			y = box_dimention[1] + box_dimention[3] + 20
			y2 = y + 443
			return (x,y,x2,y2)
	def find(self,item_to_find,expected_y):
			dimention = self.get_box_dimention()

			if expected_y:
				print("expected_y = ", expected_y)
				self.move.move((randint(dimention[0],dimention[2]),randint(expected_y-2,expected_y+2)),2  )
				cp = pyautogui.position()
				if item_to_find in readbox.read(cp[0]+5,cp[1]+20,cp[0]+150,cp[1]+30):
					print(pyautogui.position()[1])
					print('poszlo z pamieci')
					return pyautogui.position()[1]

						
			y_switch = dimention[1]
			direction = 0
			while True:

				if direction==0:
					y_switch += randint(5,15)
					if y_switch >= dimention[3]:
						print("1")
						direction = 1
				else:
					y_switch -= randint(5,15)
					if y_switch <= dimention[1]:
						print("0")
						direction = 0
				#self.move.move(,5))				
				pyautogui.moveTo(randint(dimention[0],dimention[2]),y_switch, 0.001, pyautogui.easeInQuad)
				cp = pyautogui.position()
				if item_to_find in readbox.read(cp[0]+5,cp[1]+20,cp[0]+150,cp[1]+30):
					print(cp[1])
					return cp[1]




#test = FindItem('media/box-titles/pile-of-items.png')
#print(test.get_box_dimention())
#test.find("w")

cp = pyautogui.position() # current mouse position
print( readbox.read(cp[0]+5,cp[1]+20,cp[0]+150,cp[1]+30) )
