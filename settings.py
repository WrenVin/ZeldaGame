WHITE = (255, 255, 255)
import pygame as pg
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 153, 51)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SPRITESHEETPLAYER = 'character.png'
SPRITESHEETWORLD = 'Overworld.png'
WIDTH = 800   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 600  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Trial of the Sword"
BGCOLOR = DARKGREY
FONT_NAME = 'arial'
ORANGE = (255,165,0)
TILESIZE = 40
TILEPIXEL = 16
GRIDWIDTH = WIDTH / TILESIZE

GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_SPEED = 10
PLAYER_IMG_NORMAL = [1, 7, 14, 22]
PLAYER_IMG_LEFT = [1, 102, 14, 22]
PLAYER_IMG_RIGHT = [2, 38, 14, 22]
PLAYER_IMG_UP = [1, 69, 14, 22]
BORDER = [564, 129, 24, 28]
GRASS = [450, 250, 32, 32]
PLAYER_ROT_SPEED = 250

#Animations
ANIMATIONSPEED = 100
WALKDOWN1 = [1, 6, 15, 22]
WALKDOWN2 = [17, 6, 15, 22]
WALKDOWN3 = [33, 6, 15, 22]
WALKDOWN4 = [49, 6, 15, 22]

WALKRIGHT1 = [2, 38, 13, 22]
WALKRIGHT2 = [18, 38, 14, 22]
WALKRIGHT3 = [34, 38, 14, 22]
WALKRIGHT4 = [50, 38, 14, 22]

WALKLEFT1 = [1, 102, 14, 22]
WALKLEFT2 = [17, 102, 14, 22]
WALKLEFT3 = [33, 102, 14, 22]
WALKLEFT4 = [49, 102, 14, 22]

WALKUP1 = [0, 69, 15, 23]
WALKUP2 = [16, 69, 15, 23]
WALKUP3 = [32, 69, 15, 23]
WALKUP4 = [48, 69, 15, 23]

ATTACKDOWN1 = [7, 134, 18, 21]
ATTACKDOWN2 = [40, 134, 18, 23]
ATTACKDOWN3 = [72, 134, 18, 25]
ATTACKDOWN4 = [104, 134, 16, 33]

ATTACKUP1 = [8, 166, 17, 21]
ATTACKUP2 = [40, 166, 17, 21]
ATTACKUP3 = [72, 166, 17, 21]
ATTACKUP4 = [104, 166, 17, 21]

ATTACKRIGHT1 = [9, 198, 16, 22]
ATTACKRIGHT2 = [41, 198, 20, 22]
ATTACKRIGHT3 = [73, 198, 15, 22]
ATTACKRIGHT4 = [105, 198, 15, 22]

ATTACKLEFT1 = [9, 229, 13, 23]
ATTACKLEFT2 = [40, 230, 15, 22]
ATTACKLEFT3 = [68, 229, 18, 23]
ATTACKLEFT4 = [101, 229, 18, 23]

WOODEN_SWORD = [73, 60, 16, 7]
METAL_SWORD = [9, 0, 19, 7]
EPIC_SWORD = [73, 8, 17, 9]