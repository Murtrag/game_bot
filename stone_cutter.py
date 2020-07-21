from status import Status_Bar
from pyclick import HumanClicker # super symulacja ruchu myszki
import pyautogui
import time
from random import randint, random
from lib.craft import Crafting
from lib.window import Window
mouse = HumanClicker()
status = Status_Bar()

t = Crafting(button='media/box-titles/create.png')
source = Window(title='media/box-titles/source.png')
inventory = Window(title='media/box-titles/inventory.png')
target = Window(title='media/box-titles/target.png')

while True:
    if status.stamin:
        t.continue_()
        # Get resources
        s_s = source.find_item(item="media/items/stone_shards.png")
        mouse.move((s_s[0][0],s_s[0][1]),2 ) 
        pyautogui.mouseDown()
        inventory_workspace = inventory.get_workspace()
        mouse.move((inventory_workspace['left'],inventory_workspace["top"]+inventory_workspace["height"]),2 ) 
        pyautogui.mouseUp()
        time.sleep(random()*2.5)
        pyautogui.press('enter')

        # Add resources to Crafting window and combine it
        s_b = inventory.find_item(item="media/items/stone_shards.png")
        mouse.move((s_b[0][0],s_b[0][1]),2 ) 
        pyautogui.mouseDown()
        r_p = t.get_resource_position()
        mouse.move(r_p, 2) 
        pyautogui.mouseUp()
        t.combine()

        # produce some bricks
        t.continue_()


        # Storage done products
        if status.stamin:
            s_b = inventory.find_item(item="media/items/stone_brick.png")
            mouse.move((s_b[0][0],s_b[0][1]),2 ) 
            pyautogui.mouseDown()
            target_workspace = target.get_workspace()
            mouse.move((target_workspace['left'],target_workspace["top"]+target_workspace["height"]),2 ) 
            pyautogui.mouseUp()





        
        # pyautogui.mouseUp()
        # t.combine()
        # t.get_resource_position()
        # time.sleep(random()*2)
    
