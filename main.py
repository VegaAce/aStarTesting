import pygame
from aStar import *

resolution = (1000, 1000)

pygame.init()
screen = pygame.display.set_mode(resolution)
background = pygame.Surface(resolution)
pygame.display.flip
while(True):
    screen.blit(background,(0,0))
