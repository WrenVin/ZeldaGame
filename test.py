import pygame
from pygame.locals import *
import random

WIDTH = 800
HEIGHT = 600
FPS = 304
from pytmx import load_pygame, TiledTileLayer



TILESIZE = 40
ANIMATIONSPEED = 150
#SIZE = (500, 500)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.toggle_fullscreen()
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

tmxdata = load_pygame('img/FirstMap.tmx')
print(tmxdata.get_tile_properties(2, 0, 0)['Name'])
#print(tmxdata.get_tile_properties(0, 0, 0))



#Game Loop
running = True
while running:
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    #update
    #Draw / Render
    screen.fill(BLACK)
    for i in range(50):
        for b in range(50):
            image = tmxdata.get_tile_image(b, i, 0)
            image = pygame.transform.scale(image, (40, 40))
            image.set_colorkey(BLACK)
            screen.blit(image, (b*40, i*40))

    pygame.display.flip()



pygame.quit()