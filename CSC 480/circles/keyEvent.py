import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()
H = 800
W = 600
s1 = (H/2)
s2 = (W/2)
screen = pygame.display.set_mode((H, W), 0 , 32)
pygame.display.set_caption("Movement Example")

#Here we will create the circle
radius = 96
center = (radius,radius)
width = 0 #Fills circle completely
color = (250,0,0) #Red circle

pygame.display.flip()
pygame.key.set_repeat(10,50)

while True:
    

    #Draw circle in memory


    for event in pygame.event.get():
        if (event.type == KEYDOWN):
            if event.key == K_LEFT:
                print "Left"
                s1 -= 10
            elif event.key == K_RIGHT:
                print "Right"
                s1 += 10
            elif event.key == K_UP:
                print "Up"
                s2 -= 10
            elif event.key == K_DOWN:
                print "Down"
                s2 += 10
            elif event.key == K_ESCAPE:
                os._exit(99)
                
        screen.fill((0,0,0))
        char = pygame.draw.circle(screen,color,(s1,s2),radius,width)

            
        #pygame.display.update()
        pygame.display.flip()
    
