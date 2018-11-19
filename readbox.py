from PIL import Image
import pyscreenshot as ImageGrab
import pytesseract
import os
if os.path.isfile("tmp.jpg"):
	os.remove("tmp.jpg")

def read(x1,y1,x2,y2):
    im=ImageGrab.grab(bbox=((x1,y1,x2,y2)))
                #im.show()
    im.save("tmp.jpg")
    readed= pytesseract.image_to_string(Image.open('tmp.jpg'), lang='eng')
    os.remove("tmp.jpg")
    return readed
def test(x1,y1,x2,y2):
    im=ImageGrab.grab(bbox=((x1,y1,x2,y2)))
    im.show()

