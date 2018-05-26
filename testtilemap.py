import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

colours = {
	DIRT: BROWN,
	GRASS: GREEN,
	WATER: BLUE,
	COAL:BLACK
}

tilemap=[
	[GRASS, COAL, DIRT],
	[WATER, WATER, GRASS],
	[COAL, GRASS, WATER],
	[DIRT, GRASS, COAL],
	[GRASS, WATER, DIRT]
]

TILESIZE = 40
MAPWIDTH = 3
MAPHEIGHT = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

	pygame.display.update()		
