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

txmdata = load_pygame('img/FirstMap.tmx')




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
    
    for x in range(0, 1):
            for i in range(txmdata.height):
                for b in range(txmdata.width):
                    try:
                        if txmdata.get_tile_properties(b, i, 1)['Type'] == 'Wall':
                            screen.blit(txmdata.get_tile_image(b, i, x), b, i)
                            #Wall(i, txmdata.get_tile_image(b, i, 1))
                        elif txmdata.get_tile_properties(b, i, 1)['Type'] == 'Ground':
                            screen.blit(txmdata.get_tile_image(b, i, x), b, i)
                         #Ground(i, txmdata.get_tile_image(b, i, 1))
                    except  TypeError:
                        pass

    pygame.display.flip()



pygame.quit()