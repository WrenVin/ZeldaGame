WHITE = (255, 255, 255)
import pygame as pg
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SPRITESHEETPLAYER = 'character.png'
SPRITESHEETWORLD = 'Overworld.png'
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY
GAMEMAP = 'EasyMap.txt'

TILESIZE = 60
GRIDWIDTH = WIDTH / TILESIZE

GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_SPEED = 300
PLAYER_IMG_NORMAL = [1, 7, 14, 22]
PLAYER_IMG_LEFT = [1, 102, 14, 22]
PLAYER_IMG_RIGHT = [2, 38, 14, 22]
PLAYER_IMG_UP = [1, 69, 14, 22]
BORDER = [564, 129, 24, 28]
GRASS = [450, 250, 32, 32]
PLAYER_ROT_SPEED = 250
