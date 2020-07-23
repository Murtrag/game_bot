from status import Status_Bar
from pyclick import HumanClicker # super symulacja ruchu myszki
import pyautogui
import time
import random
import find_in_box
from lib.window import Window

mouse = HumanClicker()
status = Status_Bar()
mode = input("What kind of mining are you planing to do? w(wall)/v((vein)")

count = 0
while True:
        if mode=="v" or pyautogui.locateOnScreen('media/title-window/cave_wall.png', confidence=.8):
            if status.stamin:
                
                pyautogui.typewrite('l')
                count+=1
                time.sleep(random.random()*2)

                if mode == "v" and count >= random.randint(10,50):
                    pyautogui.typewrite('l')
                    time.sleep(random.random())
                    pyautogui.typewrite('l')
                    time.sleep(random.random())
                    pyautogui.typewrite('l')

                    pile_of_items = Window(title='media/box-titles/pile-of-items.png')
                    bsb = Window(title='media/box-titles/bsb.png')
                    pyautogui.typewrite('l')
                    s_s = pile_of_items.find_item(item="media/items/ore_iron.png")
                    mouse.move((s_s[0][0],s_s[0][1]),2 ) 
                    pyautogui.mouseDown()
                    bsb_workspace = bsb.get_workspace()
                    mouse.move((bsb_workspace['left'],bsb_workspace["top"]+bsb_workspace["height"]),2 ) 
                    pyautogui.mouseUp()
                    time.sleep(random.random()*2.5)
                    mouse.move((random.randint(2679,2690),random.randint(472, 490)),2 ) 
                    mouse.click()

# 2679 472


#full house pizza - weapon smithing

