from status import Status_Bar
from pyclick import HumanClicker # super symulacja ruchu myszki
import pyautogui
import time
from random import randint, random
import find_in_box
mouse = HumanClicker()

while True:
        try:
            inventory = find_in_box.FindItem('media/box-titles/backpack.png')
            inv_cord = inventory.get_box_dimention()
            print('1')
            x, y = (randint(inv_cord[0]+34, inv_cord[0]+124),randint(inv_cord[1]+20,inv_cord[1]+48))
            mouse.move((x,y),2 )
            pyautogui.doubleClick()  #dbl click first herb

            mouse.move((x+randint(1,4),y+randint(30,150)),1 )
            pyautogui.rightClick()  #open menu with mixing option
            print('2')
            time.sleep(randint(1,2))
            print('3')
            alchemy_raw = pyautogui.locateOnScreen('media/menu/alchemy.png', confidence=.8)  #find alchemy option
            alchemy_x, alchemy_y = pyautogui.center(alchemy_raw)
            print('4')


            mouse.move((randint(alchemy_x-3, alchemy_x+3),randint(alchemy_y-3,alchemy_y+3)),2 )  #mouse on alchemy position
            print('5')
            time.sleep(randint(1,2))
            print('6')

            mix_raw = pyautogui.locateOnScreen('media/menu/mix.png', confidence=.8)  #find mix option
            mix_x, mix_y = pyautogui.center(mix_raw)
            pyautogui.moveTo(randint(mix_x-3, mix_x+3),randint(mix_y-3,mix_y+3), random(), pyautogui.easeInQuad)
            # pyautogui.moveTo(randint(mix_x-3, mix_x+3),randint(mix_y-3,mix_y+3), random.random(), pyautogui.easeInQuad)
            pyautogui.click()
            print('7')

            time.sleep(randint(2,8))
        except:
            pyautogui.moveTo(inv_cord[0],inv_cord[1],0.5, pyautogui.easeInQuad)
            pyautogui.click()
