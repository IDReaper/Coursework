#Shawn Thompson
#Practice definitions 1
#CSC 360
from visual import *
from visual.controls import *
'''
from pygame.locals import *
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Control')
pygame.mouse.set_visible(0)
'''

def what():
    x = input("No Negative number pl0x: ")
    while x >= 0:
        print "Hi, you entered",x,"."
        x = input("No Negative number pl0x: ")
    else:
        print "FAIL"

def for_practice():
    s = input("Enter a number(1-99): ")
    if s > 0 and s < 100:
        for i in range(0,100,s):
            print i, i*i
    else:
        print "Please input a valid number."
        for_practice()

def beam_saber():
    myline = curve(pos=[(-100,0,0),(100,0,0)],radius=5,color=(25,25,25))
    myline = curve(pos=[(-150,0,0),(25,0,0)],radius=6,color=(0,99,135))
    myline = curve(pos=[(25,-50,0),(25,50,0)],radius=5,color=(200,200,200))
    myline = curve(pos=[(25,0,25),(50,0,0)],radius=5,color=(100,100,100))
    myline = curve(pos=[(25,0,-25),(50,0,0)],radius=5,color=(100,100,100))
    myline = curve(pos=[(-25,0,25),(50,0,0)],radius=5,color=(150,150,100))
    myline = curve(pos=[(-25,0,-25),(50,0,0)],radius=5,color=(150,150,100))
    X_lbl = label(pos=(-25,0,50), text="I am lightsaber. RAWR!", box = 0)

def axis():
    x_axis = curve(pos=[(-100,0,0),(100,0,0)],radius=5,color=(25,25,25))
    y_axis = curve(pos=[(0,-200,0),(0,300,0)],radius=5,color=(25,25,25))
    z_axis = curve(pos=[(0,0,-200),(0,0,300)],radius=5,color=(25,25,25))
    x_label = label(pos=(102,0,0), text="x", box = 0)
    y_label = label(pos=(0,303,0), text="y", box = 0)

def ball():
    #scene.lights=[]
    #lamp = local_light(pos=(50,50,50), color=color.red)
    #lamp = local_light(pos=(-50,-50,-50), color=color.blue)
    x = -25
    p = 1
    b1 = sphere(pos=(-25,0,0), radius=7,color=(250,250,0))
    x_axis = curve(pos=[(-25,0,0),(25,0,0)],radius=1,color=(25,25,25))
    pygame.key.set_repeat(2,2)
    
    while p == 1:
        #key=pygame.key.get_pressed()
        #if key[pygame.K_d]:
            #x = x + 1
            #b1.pos = (x,0,0)
            #rate(50)
        #if key[pygame.K_a]:
            #x = x - 1
            #b1.pos = (x,0,0)
            #rate(50)
            
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if event.key == K_d:
                    x= x+1
                    b1.pos = (x,0,0)
                    rate(50)                        
                elif event.key == K_a:
                    x= x-1
                    b1.pos = (x,0,0)
                    rate(50)
                else:
                    print "Key"
                    
        #for i in range(50):
            #x= x-1
            #b1.pos = (x,0,0)
            #rate(50)
        
    
    
    


        
        
    
