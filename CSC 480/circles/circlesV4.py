# this version draws only  10 circles with width = 0,1,2,...,9
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
# Next two stmts create a display window named Window of Circles
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Window of Circles")

rds = 20 # radius of circle
cntr = (rds, rds) # coordinates of center of circle
#width = 0 # width of ring of circle
color = (250,250,0) # color of circle

# next 4 stmts create 10 center and circle within a loop body
cntr_list = [ ]
for k in range(10):
    cntr_list.append((cntr[0]+k*2*rds, cntr[1]))
# next stmt creates one circle in memory but not shown in screen
    width = k  # width changes its value from 0 to 1, to 2,..., to 9
    pygame.draw.circle(screen,color,cntr_list[k], rds, width)

# next stmt display them on screen
pygame.display.update()

