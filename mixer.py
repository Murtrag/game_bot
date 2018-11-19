from status import Status_Bar
from pyclick import HumanClicker # super symulacja ruchu myszki
import pyautogui
import time
from random import randint
import find_in_box
mouse = HumanClicker()

while True:
	try:
		inventory = find_in_box.FindItem('media/box-titles/inventory.png')
		inv_cord = inventory.get_box_dimention()
		mouse.move((randint(inv_cord[0]+34, inv_cord[0]+124),randint(inv_cord[1]+30,inv_cord[1]+38)),2 )
		pyautogui.doubleClick()  #dbl click first herb

		mouse.move((randint(inv_cord[0]+34, inv_cord[0]+124),randint(inv_cord[1]+45,inv_cord[1]+54)),2 )
		pyautogui.rightClick()  #open menu with mixing option
		time.sleep(randint(1,2))
		try:
			alchemy_raw = pyautogui.locateOnScreen('media/menu/alchemy.png')  #find alchemy option
			assert alchem_raw
		except:			
			alchemy_raw = pyautogui.locateOnScreen('media/menu/alchemy2.png')  #find alchemy option
			alchemy_raw = pyautogui.locateOnScreen('media/menu/alchemy3.png')  #find alchemy option
		finally:
			alchemy_x, alchemy_y = pyautogui.center(alchemy_raw)


		mouse.move((randint(alchemy_x-3, alchemy_x+3),randint(alchemy_y-3,alchemy_y+3)),2 )  #mouse on alchemy position
		time.sleep(randint(1,2))

		mix_raw = pyautogui.locateOnScreen('media/menu/mix.png')  #find mix option
		mix_x, mix_y = pyautogui.center(mix_raw)
		pyautogui.moveTo(randint(mix_x-3, mix_x+3),randint(mix_y-3,mix_y+3), randint(1,3), pyautogui.easeInQuad)
		pyautogui.click()

		time.sleep(randint(15,17))
	except:
		pyautogui.moveTo(inv_cord[0],inv_cord[1],1, pyautogui.easeInQuad)
		pyautogui.click()