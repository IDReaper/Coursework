#Example project for assignment-2
#See pg. 7 example 1.4 in textbook
#Create a factory with a conveyor belt dropping boxes into a box.
#
#belt = box(pos=(100,50,0),length = 200, height = 0

from visual import *
from random import *

def axis():
    x_axis = curve(pos=[(-500,0,0),(500,0,0)],radius=5,color=(25,25,25))
    y_axis = curve(pos=[(0,-500,0),(0,500,0)],radius=5,color=(25,25,25))
    z_axis = curve(pos=[(0,0,-500),(0,0,500)],radius=5,color=(25,25,25))
    x_label = label(pos=(102,0,0), text="x", box = 0)
    y_label = label(pos=(0,303,0), text="y", box = 0)
    
def theBox():
    axis()
    c1 = 250
    c2 = 0
    c3 = 0
    box1 = box(pos=(1,3,5),size=(120,160,200),axis=(0,-500,0),color=(c1,c2,c3))
    x = -500
    wUt_label = label(pos=(x,0,0), text="LOLOMGWTFBBQHAHAROFLMAOSTFUGTFOWUTWUT", box=0)
    wUt_label_2 = label(pos=(0,0,x), text="GIANT ENEMY CRABS",height = 40,border = 20, font='arial', box=0)
    p = 1
    while p == 1:
        for i in range(100):
            x = x+10
            c1 = randrange(0,250,100)
            c2 = randrange(0,250,100)
            c3 = randrange(0,250,100)
            wUt_label.pos = (x,0,0)
            box1.pos = (0,x,0)
            box1.color = (c1,c2,c3)
            wUt_label_2.pos = (0,0,x)
            rate(100)
        for i in range(100):
            x = x-10
            c1 = randrange(0,250,100)
            c2 = randrange(0,250,100)
            c3 = randrange(0,250,100)
            wUt_label.pos = (x,0,0)
            box1.pos = (0,x,0)
            box1.color = (c1,c2,c3)
            wUt_label_2.pos = (0,0,x)
            rate(100)
            
def theRegularbox():
    axis()
    
    box1 = box(pos=(0,0,0),size=(10,20,30),axis=(1,0,0),color=(250,0,0))
    #axis of the box controls the angle of tilt
    #x = -500
    for x in range(0,51,5):
        box1.pos=(x, 0, 0)
        rate(0.5)
        
        
    
