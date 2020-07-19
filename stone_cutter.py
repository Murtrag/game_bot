from status import Status_Bar
from pyclick import HumanClicker # super symulacja ruchu myszki
import pyautogui
import time
from random import randint, random

mouse = HumanClicker()
status = Status_Bar()
class Crafting:
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


t = Crafting(button='media/box-titles/create.png')
while True:
    if status.stamin:
        t.continue_()
        time.sleep(random()*2)
    
