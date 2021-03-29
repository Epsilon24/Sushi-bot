# File: SushiFork.py

"""
Chrome is maximized, no toolbar, scrolled down 3 clicks so that there is
a hair of whitespace between the blue bar (games>strategy>sushi) and the 
tabs bar/url.  Im also using an adblocker, and have the chrome tab with 
the game on the left of a split single screen
"""
#Global      these are the offsets of the top-left corner
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
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

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
    tupler = (x,y)
    return tupler 

def foldMat():
    setCoords((200,350))
    time.sleep(0.1)
    leftClick()
    time.sleep(0.1)

def convertCoords(Coords):        #to be used with the im and getpixel functions
    x = Coords[0] + 135       #the getcoord and setcoord do this on their own
    y = Coords[1] + 114
    finalTuple = (x,y)
    return finalTuple

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

    for i in range(6):
        setCoords(((80+100i),166))   #might need to change the multiple of i to 101 or 102 
        leftClick()                 #since the last coord has an x-value of 592
    print("all tables clear!")

"""
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
"""

def makeFood(food):
    print("making a " + food)
    for i in range(len(Recipes[food])):
        setCoords(Coord[Recipes[food][i]])   #this line probably needs work, not sure how
        sleep(0.1)          #the nested indexing works (especially the bracket placement)
        leftClick()
        sleep(0.1)
        print("added " + Recipes[food][i]



if food == 'caliroll':
        print("making a caliroll")
        setCoords(Coord["f_rice"])
        leftClick()
        time.sleep(.05)
        setCoords(Coord["f_nori"])
        leftClick()
        time.sleep(.05)
        setCoords(Coord["f_roe"])
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print ('making an onigiri')
        setCoords(Coord["f_rice"])
        leftClick()
        time.sleep(.05)
        setCoords(Coord["f_rice"])
        leftClick()
        time.sleep(.05)
        setCoords(Coord["f_nori"])
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)

    elif food == 'gunkan':
        print ('making a gunkan')
        setCoords(Coord["f_rice"])
        leftClick()
        time.sleep(.05)
        setCoords(Coord["f_nori"])
        leftClick()
        time.sleep(.05)
        setCoords(Coord["f_roe"])
        leftClick()
        time.sleep(.05)
        setCoords(Coord["f_roe"])
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)
    

def buyFood(food):
    setCoords(Coord["phone"])
    print('test1111')

    if food == 'rice':
        leftClick()
        setCoords(Coord["menu_rice"])
        time.sleep(0.1)
        leftClick()
        setCoords(Coord["buy_rice"])
        time.sleep(0.2)
        s = screenGrab()
        print(s.getpixel((650,350)))  #
        print(s.getpixel(convertCoords(Coord["buy_rice"])))
        if (s.getpixel(convertCoords(Coord["buy_rice"])) != (118, 83, 85)):
            print ('rice is available')
            setCoords(Coord["buy_rice"])
            time.sleep(0.1)
            leftClick()
            setCoords(Coord["delivery_normal"])
            time.sleep(0.1)
            leftClick()
            time.sleep(2.5)

           
        else:
            print ('rice is NOT available')
            setCoords(Coord["t_exit"])
            leftClick()
            time.sleep(1)
            buyFood(food)
           

    else:
        leftClick()
        setCoords(Coord["menu_toppings"])
        leftClick()
        time.sleep(1)       #might need to change this
        s = screenGrab()
        print ('test')
        time.sleep(1)
        t_food = "t_" + food        #create a string to pass to setCoords of the form t_toppings
        if s.getpixel(convertCoords(Coord[t_food]))  != color:
            print ((t_food) + "is available")
            setCoords(Coord[t_food])
            time.sleep(1)
            leftClick()
            setCoords(Coord["delivery_normal"])
            time.sleep(1)
            leftClick()
            time.sleep(2)
        else:
            print (t_food + "is NOT available")
            setCoords(Coord["t_exit"])
            leftClick()
            time.sleep(1)
            buyFood(food)



Coord = {
    "f_shrimp": (40, 280),
    "f_rice": (90, 290),
    "f_nori": (35, 350),
    "f_roe": (85, 350),
    "f_salmon": (34, 401),
    "f_unagi": (90, 400),

    "mat": (206, 343),

    #########################

    "phone": (550, 315),

    "menu_toppings":(505, 235),

    "t_shrimp": (520, 170),   #  _t  prefix indicates that this item is 
    "t_nori": (516, 228),     #  in the toppings menu (when buying on phone)
    "t_roe": (547, 230),
    "t_salmon": (516, 284),
    "t_unagi": (540, 180),

    "t_exit": (584, 301),
    "menu_rice": (513, 255),
    "buy_rice": (513, 245),
    
    "delivery_normal": (485, 255),  #express is (590,255), but shouldnt be needed
}

Color = {
    "t_shrimp": (255, 250, 208),
    "t_nori": (238, 219, 169),
    "t_roe": (202, 55, 25),
    "t_salmon": (0, 0, 0),
    "t_unagi": (240, 41, 41),

    "buy_rice": (238, 219, 169),
}

Recipes = {
    "caliroll": ("rice", "nori", "roe")
    "gunkan": ("rice", "nori", "roe", "roe")
    "nori": ("rice", "rice", "nori")
    "shrimp": ("rice", "rice", "nori", "shrimp")

}


color = (109, 123, 127)
