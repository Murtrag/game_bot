from pyclick import HumanClicker 
import pyautogui
from random import randint

mouse = HumanClicker()
class Window:
    def __init__(self, title):
        self._title = title

    def _get_title_dimension(self):
         return pyautogui.locateOnScreen(self._title, confidence=.8) 
    def _get_window_image(self):
         title = self._get_title_dimension()
         return pyautogui.screenshot(region=(title.left-10,title.top, 300, 500))

    def find_item(self, item):
        title = self._get_title_dimension()

        title_x, title_y= pyautogui.center(title) 
        mouse.move((randint(title_x-30, title_x+30),randint(title_y-4,title_y+4)),2 ) 
        pyautogui.click()

        return [(randint(title.left+x.left,title.left+x.left+15),randint(title.top+x.top+3,title.top+x.top+7)) for x in pyautogui.locateAll(item, self._get_window_image(), confidence=.9)]
    
    def get_workspace(self):
        ''' Returns coordinates of any workspace '''
        title = self._get_title_dimension()
        # return pyautogui.screenshot(region=(title.left-10,title.top, 300, 500))
        return {'left':title.left, "top":title.top+30, "width":300, "height":400}
