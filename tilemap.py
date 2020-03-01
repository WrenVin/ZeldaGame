import pygame as pg
from settings import *
from os import path
from pytmx import load_pygame, TiledTileLayer
class Map:
    def __init__(self, filename):
        self.txmdata = load_pygame(filename)

        self.tilewidth = self.txmdata.width
        self.tilehieght = self.txmdata.height
        self.width = 16 * TILESIZE
        self.height = 16 * TILESIZE
    def get_tile_image(self, x, y, layer):
        img = self.txmdata.get_tile_image(x, y, layer)
        img = pg.transform.scale(img, (8, 8))
        img.set_colorkey(BLACK)
        return img
            
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
