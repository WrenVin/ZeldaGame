import pygame as pg
from settings import *
from os import path

class Map:
    def __init__(self, filename):
        game_folder = path.dirname(__file__)
        self.data = []
        with open (path.join(game_folder, GAMEMAP), 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tilehieght = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tilehieght * TILESIZE
        
        
class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width,height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(WIDTH/2)

        #limit
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pg.Rect(x, y, self.width, self.height)
