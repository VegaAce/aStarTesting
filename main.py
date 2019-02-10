import pygame
import numpy as np
import time
from aStar import astar

maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
start = (0,9)
end = (9,0)
resolution = (1000, 1000)
white = [255,255,255]
black = [0,0,0]
pygame.init()
screen = pygame.display.set_mode(resolution)
background = pygame.Surface(resolution)
pygame.display.flip()
path = astar(maze, start, end )
pygamePath = np.array(path)
pygamePath = pygamePath * 100
print(path)
while(True):
    event = pygame.event.get()
    for event in event:
        if event.type == pygame.QUIT:
            pygame.QUIT()

    thing = len(pygamePath)
    i = 0
    for x in range(thing):
        background.fill(white)

        player = pygame.draw.rect(background, black, ((pygamePath[i][0], pygamePath[i][1]),(10,10)))

        i += 1
        screen.blit(background,(0,0))
        pygame.display.update()
        time.sleep(1)
