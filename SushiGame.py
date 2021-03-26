"""
Chrome is maximized, no toolbar, scrolled down 3 clicks so that there is
a hair of whitespace between the blue bar (games>strategy>sushi) and the 
tabs bar/url.  Im also using an adblocker, and have the chrome tab with 
the game on the left of a split single screen
"""
#Globals
x_pad = 22
y_pad = 233

from numpy import *          #fun wildcard import indicated by the star
from PIL import ImageGrab
from PIL import ImageOps
import os
import time
import win32.win32api as win32api      #the tutorial just had win32api/con, no prefix
import win32.lib.win32con as win32con   #so i aliased them here to be consistent 
 
def screenGrab():
    box = (x_pad + 1,y_pad + 1,800 + x_pad , 599 + y_pad)
    im = ImageGrab.grab(bbox=box)    #DEVIANT: the tutorial said "ImageGrab.grab(box)" instead
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("click")   #for debugging only

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print("left down")

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print("left release/up")

def setCoords(coord):
    win32api.SetCursorPos((x_pad + coord[0], y_pad + coord[1]))
#using double parentheses because it passes the tuple as a tuple

def getCoords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def foldMat():
    setCoords((200,350))
    leftClick
    time.sleep(0.1)

def main():
    pass
 
if __name__ == '__main__':
    main()
 


def startGame():
    setCoords((320,170))  #load button (bugged rn, since it takes a variable amt
    leftClick()           #of time to load
    time.sleep(.1)

    setCoords((320,170))  #continue button
    leftClick()
    time.sleep(.1)

    setCoords((290,349))  #bypass phone ad
    leftClick()
    time.sleep(.1)

    setCoords((576,409))  #skip tutorial
    leftClick()
    time.sleep(.1)

    setCoords((316,329))  #final button: continue to game
    leftClick()
    time.sleep(.1)


def clearTables():
    setCoords((80,161))
    leftClick()

    setCoords((180,165))
    leftClick()

    setCoords((280,166))
    leftClick()

    setCoords((380,166))
    leftClick()
 
    setCoords((480,166))
    leftClick()

    setCoords((592,168))
    leftClick()

def makeFood(food):
    if food == 'caliroll':
        print("making a caliroll")
        setCoords(Coord.f_rice)
        leftClick()
        time.sleep(.05)
        setCoords(Coord.f_nori)
        leftClick()
        time.sleep(.05)
        setCoords(Coord.f_roe)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print ('making an onigiri')
        setCoords(Coord.f_rice)
        leftClick()
        time.sleep(.05)
        setCoords(Coord.f_rice)
        leftClick()
        time.sleep(.05)
        setCoords(Coord.f_nori)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)

    elif food == 'gunkan':
        print ('making a gunkan')
        setCoords(Coord.f_rice)
        leftClick()
        time.sleep(.05)
        setCoords(Coord.f_nori)
        leftClick()
        time.sleep(.05)
        setCoords(Coord.f_roe)
        leftClick()
        time.sleep(.05)
        setCoords(Coord.f_roe)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)

def buyFood(food):
    setCoords(Coord.phone)

    setCoords(Coord.menu_toppings)

    setCoords(Coord.t_shrimp)
    setCoords(Coord.t_nori)
    setCoords(Coord.t_roe)
    setCoords(Coord.t_salmon)
    setCoords(Coord.t_unagi)
    setCoords(Coord.t_exit)   #still need to scrape this coord!

    setCoords(Coord.menu_rice)
    setCoords(Coord.buy_rice)

    setCoords(Coord.delivery_normal)


class Coord:
    f_shrimp = (40, 280)
    f_rice = (90, 290)
    f_nori = (35, 350)
    f_roe = (85, 350)
    f_salmon = (34, 401)
    f_unagi = (90, 400)

    mat = (206, 343)

    #########################

    phone = (550, 315)

    menu_toppings = (505, 235)

    t_shrimp = (490, 180)   #  _t  prefix indicates that this item is 
    t_nori = (478, 235)      #  in the toppings menu (when buying on phone)
    t_roe = (570, 240)
    t_salmon = (485, 290)
    t_unagi = (565, 180)

    menu_rice = (513, 255)
    buy_rice = (513, 255)

    delivery_normal = (485, 255)  #express is (590,255), but shouldnt be needed


"""
>>> getCoords()#phoneTopping
506 233
>>> getCoords()#phoneRice
513 255
>>> getCoords()#phoneSake
500 281
>>> getCoords()#sushi mat
206 343
>>> startGame()
click
click
click
click
click
>>> getCoords()#plate1
80 161
>>> getCoords()#2
180 165
>>> getCoords()#3
280 166
>>> getCoords()#4
382 161
>>> getCoords()#5
477 162
>>> getCoords()#6
592 168
>>> getCoords()
579 169

>>> getCoords()#shrimp
487 168
>>> getCoords()
490 181
>>> getCoords()#beef
567 180
>>> getCoords()#nori
478 235
>>> getCoords()#roe
568 242
>>> getCoords()#salmon
485 291
>>> getCoords()#rice menu
517 256
>>> #rice has the same coords
>>> getCoords()#delivery: free
483 254
>>> getCoords()#delivery: express
587 255
>>> 
"""