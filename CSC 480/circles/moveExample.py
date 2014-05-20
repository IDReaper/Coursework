import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()
H = 800
W = 600
S_Center = (H/2, W/2)
screen = pygame.display.set_mode((H, W), 0 , 32)
pygame.display.set_caption("Movement Example")

#Here we will create the circle
radius = 96
center = (radius,radius)
width = 0 #Fills circle completely
color = (250,0,0) #Red circle
    
while True:
    

    #Draw circle in memory


    for event in pygame.event.get():
        if (event.type == KEYDOWN):
            if event.key == K_LEFT:
                print "Left"
                char.getCenter()
                x = char.getCenter() - 10
                char.move(x,0)
            elif event.key == K_RIGHT:
                print "Right"
            elif event.key == K_UP:
                print "Up"
            elif event.key == K_DOWN:
                print "Down"
            elif event.key == K_ESCAPE:
                os._exit(99)
                
            
    char = pygame.draw.circle(screen,color,S_Center,radius,width)
    
    pygame.display.update()
