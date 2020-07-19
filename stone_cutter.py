from status import Status_Bar
from pyclick import HumanClicker # super symulacja ruchu myszki
import pyautogui
import time
from random import randint, random

mouse = HumanClicker()
status = Status_Bar()
while True:
    if status.stamin:
        button = pyautogui.locateOnScreen('media/box-titles/continue.png', confidence=.8) 
        button_x, button_y = pyautogui.center(button)
        mouse.move((randint(button_x-30, button_x+30),randint(button_y-3,button_y+3)),2 ) 
        pyautogui.click()
        time.sleep(random()*2)
    
