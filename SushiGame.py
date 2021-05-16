# File: SushiFork.py

"""
Chrome is maximized, no toolbar, scrolled down 3 clicks so that there is
a hair of whitespace between the blue bar (games>strategy>sushi) and the 
tabs bar/url.  Im also using an adblocker, and have the chrome tab with 
the game on the left of a split single screen
"""
#Global      these are the offsets of the top-left corner
x_pad = 19   
#y_pad = 195
y_pad = 199

#changed x_pad by -3, y_pad by -38 

from numpy import *          #fun wildcard import indicated by the star
from PIL import ImageGrab
from PIL import ImageOps
import os
import time
import win32.win32api as win32api      #the tutorial just had win32api/con, no prefix
import win32.lib.win32con as win32con   #so i aliased them here to be consistent 
 
def screenGrab():
    box = (x_pad + 1,y_pad + 48,800 + x_pad , 637 + y_pad)
    im = ImageGrab.grab(bbox=box)    #DEVIANT: the tutorial said "ImageGrab.grab(box)" instead
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def Grab():
    box = (x_pad + 1,y_pad + 1,800 + x_pad , 599 + y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(bbox=box))    #DEVIANT: the tutorial said "ImageGrab.grab(box)" instead
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    return a

def leftClick():
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.05)
    
    #print("click")   #for debugging only

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
    finalTuple = ((x,y))
    return finalTuple

def checkFood():
    for i, j in foodOnHand.items():
        if j <= 4:
            print ("%s is low and needs to be resupplied" % i) 
            buyFood(i)

#todo: subtract a certain amount from the get_order coords, shown by the difference between 
#the pictures in the "stuff" doc.  difference: 39

def checkMat(slot):
    blank_color = 229
    box_array = [178, 590, 374, 785]
    im = ImageGrab.grab(bbox=box_array)  
    
    im = ImageOps.grayscale(ImageGrab.grab(bbox=box_array))
    if im.getpixel((matLocation[slot])) == blank_color:
        return False
    else:
        return True



matBox = ((159,391),(355,586))


def getOrder():
    a_array = []
    box_array = [0,0,0,0]
    for i in range(6):
        box_array[0] = (orderLocations[i][0] + x_pad)
        box_array[1] = (orderLocations[i][1] + y_pad + 38)
        box_array[2] = (orderLocations[i][2] + x_pad)
        box_array[3] = (orderLocations[i][3] + y_pad + 38)
        box = ((box_array[0], box_array[1], box_array[2], box_array[3]))
        im = ImageOps.grayscale(ImageGrab.grab(bbox=box))
        a = array(im.getcolors())


        b = []

        a_flat = a.flat 

        for j in a_flat:
            if j < 255:
                b.append(j)

        
        
        a_mean = round(mean(b), 2)
        print (a_mean)
        a_array.append(a_mean)
        

        #im.save(os.getcwd() + "\\seat_" + str(i) + "__" + str(int(time.time())) + ".png", "PNG")
    return(a_array)

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

    setCoords((290,369))  #bypass phone ad  #changed down by 20 because it wasn't working, original y-value of 349
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
        setCoords(((80 + (100*i) ), 204))   #might need to change the multiple of i to 101 or 102 
        leftClick()                 #since the last coord has an x-value of 592
    print("all tables clear!")

def makeFood(food):
    print("making a " + food)
    time.sleep(0.1)
    for i in range(len(Recipes[food])):
        while True:
            temp = ([Recipes[food][i]])
            setCoords(Coord["f_" + str(temp[0])])  #this line probably needs work, not sure how
            time.sleep(0.1)                        #the nested indexing works (especially the bracket placement) 
            leftClick()
            foodOnHand[Recipes[food][i]] -= 1
            if checkMat(i) == True:
                break
    foldMat()

def buyFood(food):
    setCoords(Coord["phone"])
    print('test1111')

    if food == 'rice':            #rice buying seems broken, need to lower mouse coords a bit
        leftClick()
        setCoords(Coord["menu_rice"])
        time.sleep(0.2)
        leftClick()
        setCoords(Coord["buy_rice"])
        time.sleep(0.2)
        s = screenGrab()
        print(s.getpixel(convertCoords(Coord["buy_rice"])))
        if (s.getpixel(convertCoords(Coord["buy_rice"])) != (118, 83, 85)):
            print ('rice is available')
            setCoords(Coord["buy_rice"])
            time.sleep(0.2)
            leftClick()
            setCoords(Coord["delivery_normal"])
            time.sleep(0.2)
            leftClick()
            foodOnHand["rice"] += 10

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
        time.sleep(0.3)       #might need to change this
        s = screenGrab()
        print ('test')
        time.sleep(0.3)
        t_food = "t_" + food        #create a string to pass to setCoords of the form t_toppings
        if s.getpixel(convertCoords(Coord[t_food]))  != color:
            print ((t_food) + "is available")
            setCoords(Coord[t_food])
            time.sleep(0.3)
            leftClick()
            setCoords(Coord["delivery_normal"])
            time.sleep(0.3)
            leftClick()
            if (food == "unagi") or (food == "salmon") or (food == "shrimp"):
                foodOnHand[food] += 5

            else:
                foodOnHand[food] += 10
            
        else:
            print (t_food + "is NOT available")
            setCoords(Coord["t_exit"])
            leftClick()
            time.sleep(1)
            buyFood(food)

def mainLoop():
    orders = getOrder()
    print("step 1")
    for i in range(6):
        if (i % 2) == 1:
            clearTables()
        checkFood()
        print("step" + str(i))
        if orders[i] == foodLocations["blank"][i]:
            print("nothing")
        else:
            for food in foodLocations:
                print(food)
                if foodLocations[food][i] == orders[i]:
                    makeFood(food)


def playGame():
    while True:
        mainLoop()

    




Coord = {
    "f_shrimp": (40, 318),
    "f_rice": (90, 328),
    "f_nori": (35, 388),
    "f_roe": (85, 388),
    "f_salmon": (34, 439),
    "f_unagi": (90, 438),

    "mat": (206, 343),

    #########################   changed y-pads but not x pads, this shouldnt matter

    "phone": (550, 348),

    "menu_toppings":(505, 273),

    "t_shrimp": (520, 208),   #  _t  prefix indicates that this item is 
    "t_nori": (516, 266),     #  in the toppings menu (when buying on phone)
    "t_roe": (547, 268),
    "t_salmon": (516, 322),
    "t_unagi": (540, 218),

    "t_exit": (584, 339),
    "menu_rice": (513, 293),
    "buy_rice": (513, 283),
    
    "delivery_normal": (485, 283),  #express is (590,255), but shouldnt be needed
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
    "caliroll": ("rice", "nori", "roe"),
    "gunkan": ("rice", "nori", "roe", "roe"),
    "onigiri": ("rice", "rice", "nori"),
    "shrimp_roll": ("rice", "rice", "nori", "shrimp"),
    "salmon_roll": ("rice", "rice", "nori", "salmon"),
    "unagi_roll": ("rice", "rice", "nori", "unagi"),
    
}

foodOnHand = {
    'shrimp':5,
    'rice':10,
    'nori':10,
    'roe':10,
    'salmon':5,
    'unagi':5
}

orderLocations = {   #define boxes, in format (topleft x, topleft y, bottomright x, bottomleft y)
    0: (34, 86, 114, 103),  #moved right by 2
    1: (160, 86, 237, 103),
    2: (288, 86, 365, 103),  #moved right by 2
    3: (412, 86, 489, 103),
    4: (539, 86, 616, 103),
    5: (665, 86, 742, 103),
}

foodLocations = {
    "blank": (111.18, 111.37, 89.95, 94.89, 102.86, 108.1),
    "caliroll": (92.03, 94.85, 0, 93.94, 92.03, 94.85),
    "onigiri": (86.19, 0, 85.42, 88.77, 86.19, 84.1),
    "gunkan": (80.23, 81.81, 85.42, 81.7, 80.23, 81.81)
}

color = (109, 123, 127)

matLocation = [
    (41,88),
    (96,88),
    (156,88),
    (41,138),
    (96,138),
    (156,138),
]