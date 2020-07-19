from status import Status_Bar
from pyclick import HumanClicker # super symulacja ruchu myszki
import pyautogui
import time
import random
import find_in_box

mouse = HumanClicker()
#
status = Status_Bar()
mode = input("What kind of mining are you planing to do? w(wall)/v((vein)")

count = 0
while True:
        # if pyautogui.position()[0]>1919 and pyautogui.position()[1]<922:
        if pyautogui.locateOnScreen('media/title-window/cave_wall.png', confidence=.8):
        # if True:
            print('cave wall jest')
            if status.stamin:
                pyautogui.typewrite('l')
                count+=1
                # time.sleep(random.randint(13,20))
                time.sleep(random.random()*2)

                if mode == "v" and count >= random.randint(10,50):
                    pyautogui.typewrite('j')
                    poi = find_in_box.FindItem('media/box-titles/pile-of-items.png') # pile of item
                    try:
                        expected_y = poi.find("are",expected_y)
				
                    except NameError:
                        expected_y = poi.find("are",False)

                        pyautogui.mouseDown()
                        mouse.move((random.randint(2700,2950),random.randint(400,600)),2 )
                        pyautogui.mouseUp()
                        mouse.move((random.randint(3100,3120),random.randint(336,640)),2)
                        pyautogui.click()
                        mouse.move((random.randint(3100,3120),random.randint(336,640)),2)
                        count=0



#while True:
#	if status.stamin:
#		location = pyautogui.locateOnScreen("media/box-titles/continue.png")
#		mouse.move((random.randint(location[0],location[0]+location[2]),random.randint(location[1],location[1]+location[3])),2)
#		pyautogui.click()
#	if random.randint(1,5)==random.randint(1,5):
#		mouse.move((random.randint(0,4000),random.randint(0,1900)),2)



#full house pizza - weapon smithing

