from visual import *
from visual.controls import *
from pygame.locals import *
import pygame
from random import *
import sys

#sirl33t@gmail.com

def axis():
    x_axis = curve(pos=[(-200,0,0),(200,0,0)],radius=5,color=(25,25,25))
    y_axis = curve(pos=[(0,-200,0),(0,200,0)],radius=5,color=(25,25,25))
    z_axis = curve(pos=[(0,0,-200),(0,0,200)],radius=5,color=(25,25,25))
    x_label = label(pos=(202,0,0), text="x", box = 0)
    y_label = label(pos=(0,202,0), text="y", box = 0)
    z_label = label(pos=(0,0,202), text="z", box = 0)

def factory():
    #print "In progress"
    wallLeft = box(pos=(0,0,0), length = 1, height = 100, width = 100,color=(250,0,0))
    wallRight = box(pos=(100,0,0), length = 1, height = 100, width = 100,color=(250,0,0))
    wallBack = box(pos=(50,0,50), length = 100, height = 100, width = 1,color=(250,0,0))
    roofLeft = box(pos=(0,50,0),axis = (50,-50,0), length = 1, height = 50, width = 100)
    roofRight = box(pos=(100,50,0),axis = (50,50,0), length = 1, height = 50, width = 100)
    roofTop = box(pos=(50,68,0), length = 65, height = 1, width = 100)
    wallFront1 = box(pos=(87.5,0,-50),length = 25, height = 100, width = 1,color=(250,0,0))
    wallFront2 = box(pos=(12.5,0,-50),length = 25, height = 100, width = 1,color=(250,0,0))
    wallFront3 = box(pos=(50,-20,-50),length = 50, height = 60, width = 1,color=(250,0,0))

def conveyor():
    #print "In progress"
    conveyer = box(pos=(50,10,-50), length = 50, height = 1, width = 150)

def ground():
    ground = box(pos=(50,-50,0), length = 700, height = 1, width = 700, color = (0,250,0))

def pillars():
    post1 = cylinder(pos=(25,-50,-100),axis=(0,75,0),radius = 1, height = 20, color=(0,0,250))
    post2 = cylinder(pos=(75,-50,-100),axis=(0,75,0),radius = 1, height = 20, color=(0,0,250))


def box5kg():
    print "In progress"
    box1 = box(pos=(50,12.5,0), length = 5, height = 5, width = 5,color = (250,250,0))
    y = 12.5
    z = 0    
    time.sleep(3)
    for i in range(127):
        z = z-1
        box1.pos = (50,12.5,z)
        rate(50)
    for i in range(50):
        y = y-1
        box1.pos = (50,y,z)
        rate(50)
    time.sleep(3)
    box1.opacity = (0)

def box10kg():
    print "In progress"
    box1 = box(pos=(50,15,0), length = 10, height = 10, width = 10,color = (250,250,0))
    y = 15
    z = 0    
    time.sleep(3)
    for i in range(130):
        z = z-1
        box1.pos = (50,15,z)
        rate(50)
    for i in range(50):
        y = y-1
        box1.pos = (50,y,z)
        rate(50)
    time.sleep(3)
    box1.opacity = (0)

def box15kg():
    print "In progress"
    box1 = box(pos=(50,17.5,0), length = 15, height = 15, width = 15,color = (250,250,0))
    y = 17.5
    z = 0    
    time.sleep(3)
    for i in range(133):
        z = z-1
        box1.pos = (50,17.5,z)
        rate(50)
    for i in range(50):
        y = y-1
        box1.pos = (50,y,z)
        rate(50)
    time.sleep(3)
    box1.opacity = (0)

def start():
    factory()
    conveyor()
    ground()
    pillars()
    total = 0
    count = 0
    box1Count = 0
    box2Count = 0
    box3Count = 0
    go = 1
    while go == 1:
        boxSelect = input("Which box would you like to send?(5,10,15, or any other number to end): ")
        if boxSelect == 5:
            box5kg()
            count = count + 1
            total = total + 5
            box1Count = box1Count+1
            print "You have added a 5kg box to the package."
        elif boxSelect == 10:
            box10kg()
            count = count + 1
            total = total + 10
            box2Count = box2Count+1
            print "You have added a 10kg box to the package."
        elif boxSelect == 15:
            box15kg()
            count = count + 1
            total = total + 15
            box3Count = box3Count+1
            print "You have added a 15kg box to the package."
        else:
            print "Process Ended"
            print "You have added", count,"boxes and the total package weight is", total,"kg."
            print "5kg:",box1Count
            print "10kg:",box2Count
            print "15kg:",box3Count
            again = input("Press 1 to resart, any other key to quit: ")
            if again == 1:
                print "Resatarting..."
                time.sleep(3)
                total = 0
                count = 0
            break
    print "Program End"

def start_rand():
    factory()
    conveyor()
    ground()
    pillars()
    total = 0
    count = 0
    box1Count = 0
    box2Count = 0
    box3Count = 0
    box_list = []
    inBox = input("Please enter the number of boxes you wish to process: ")
    for i in range(inBox):
        rndBox = randrange(0,3,1)
        if rndBox == 0:
            box_list.append(5)
            print "A 5kg box has been created."
            time.sleep(1)
        elif rndBox == 1:
            box_list.append(10)
            print "A 10kg box has been created."
            time.sleep(1)
        elif rndBox == 2:
            box_list.append(15)
            print "A 15kg box has been created."
            time.sleep(1)
    print box_list[0:], "are the weight of the boxes that have arrived."
    begin = input("Enter 1 to process boxes, any other number to end: ")
    if begin == 1:
        boxNum = 0
        box_list[boxNum]
        while inBox != 0:
            if box_list[boxNum] == 5:
                box5kg()
                count = count + 1
                total = total + 5
                box1Count = box1Count+1
                boxNum=boxNum+1
                inBox = inBox - 1
                print "You have added a 5kg box to the package."
            elif box_list[boxNum] == 10:
                box10kg()
                count = count + 1
                total = total + 10
                box2Count = box2Count+1
                boxNum=boxNum+1
                inBox = inBox - 1
                print "You have added a 10kg box to the package."
            elif box_list[boxNum] == 15:
                box15kg()
                count = count + 1
                total = total + 15
                box3Count = box3Count+1
                boxNum=boxNum+1
                inBox = inBox - 1
                print "You have added a 15kg box to the package."
            else:
                break
        
        print "Process Ended"
        print "You have added", count,"boxes and the total package weight is", total,"kg."
        print "5kg:",box1Count
        print "10kg:",box2Count
        print "15kg:",box3Count
        again = input("Press 1 to resart, any other key to quit: ")
        if again == 1:
            print "Resatarting..."
            time.sleep(3)
            start_rand()    
    else:
        print "Program End"
        
        
        
        
    
