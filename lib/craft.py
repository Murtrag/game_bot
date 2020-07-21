from pyclick import HumanClicker 
import pyautogui
from random import randint

mouse = HumanClicker()
class Crafting:
    clicks = 0

    def __init__(self, button):
        self._button_r = button

    @property
    def _button(self):
        return pyautogui.locateOnScreen(self._button_r, confidence=.8) 

    @property
    def _button_x(self):
        return pyautogui.center(self._button)[0]

    @property
    def _button_y(self):
        return pyautogui.center(self._button)[1]

    def continue_(self):
        mouse.move((randint(self._button_x-30, self._button_x+30),randint(self._button_y-3,self._button_y+3)),2 ) 
        pyautogui.click()

    @property
    def _hand(self):
        hand =  pyautogui.locateOnScreen('media/items/hand.png', confidence=.8) 
        return pyautogui.center(hand)

    def combine(self):
        x,y = self._hand
        x+=65
        y+=22
        mouse.move((randint(x-3, x+3),randint(y-3,y+3)),2 ) 
        pyautogui.click()
        Crafting.clicks+=1

    def get_resource_position(self):
        x,y = self._hand
        # mouse.move((randint(x+16,x+49),randint(y+2,y+27)),2 ) 
        return (randint(x+16,x+49), randint(y+2,y+27))


