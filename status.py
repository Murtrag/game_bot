import pyautogui

class Status_Bar:
	def __init__(self):
		pass

	@property
	def stamin(self):
		'''Returns True or False depends od stamina status 100% - True'''
		if  pyautogui.locateOnScreen('media/status-bar/stamina.png'):
			return True
		else:
			return False
	@property
	def hunger(self):
		'''Returns True or False depends od food bar status 80% - True'''
		if  pyautogui.locateOnScreen('media/status-bar/hunger.png', confidence=.8):
			return False
		else:
			return True

	@property
	def thirst(self):
		'''Returns True or False depends od drink bar status 80% - True'''
		if  pyautogui.locateOnScreen('media/status-bar/thirst.png', confidence=.8):
			return True
		else:
			return False
	
	


#test = Status_Bar()
#print(test.hunger)

#STAMIN = pyautogui.center(pyautogui.locateOnScreen('media/status-bar/stamina.png'))
#print(STAMIN)

