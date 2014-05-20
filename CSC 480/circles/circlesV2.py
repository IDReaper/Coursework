# this version draws only  10 circles 
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
# Next two stmts create a display window named Window of Circles
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Window of Circles")

rds = 20 # radius of circle
cntr = (rds, rds) # coordinates of center of circle
width = 2 # width of ring of circle
color = (250,250,0) # color of circle

# next 3 stmts create 10 centers
cntr_list = [ ]
for k in range(10):
    cntr_list.append((cntr[0]+k*2*rds, cntr[1]))
    # Note that the second coord of all 10 cntr are the same.
    # so that the circles all line up horizontally


# next stmt draws 10 circles in memory but not shown in screen
for k in range(10):
    pygame.draw.circle(screen,color,cntr_list[k], rds, width)

# next stmt displays them on screen
pygame.display.update()

#Your assignments:
# 1. Revise the program, so that all 10 circles will line up at bottom
#    of screen.
#
# 2. all circles will line up vertically, 10 on left, and 10 on right
#    boarder of the screen.
