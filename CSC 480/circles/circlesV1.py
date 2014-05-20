import pygame
from pygame.locals import *
from sys import exit

pygame.init()
# Next two stmts create a display window named Window of Circles
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Window of Circles")

pygame.draw.circle(screen,(250,250,0),(10,10), 10, 5)
