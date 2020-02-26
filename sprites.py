import pygame as pg
vec = pg.math.Vector2
from settings import *

class SpriteSheet:
    #Utility for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()
        
    def get_image(self, x, y, width, height):
        #Gets image off sprite sheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        image = pg.transform.scale(image, (width*2, height*2))
        image.set_colorkey((BLACK))
        return image
    
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        #self.image.set_colorkey((BLACK))
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0


    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot = 180
            self.game.player_img = self.game.playerspritesheet.get_image(*PLAYER_IMG_LEFT)
            self.vel = vec(PLAYER_SPEED / 2, 0).rotate(-self.rot)
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot = 360
            self.game.player_img = self.game.playerspritesheet.get_image(*PLAYER_IMG_RIGHT)
            self.vel = vec(PLAYER_SPEED / 2, 0).rotate(-self.rot)
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.rot = 90
            self.game.player_img = self.game.playerspritesheet.get_image(*PLAYER_IMG_UP)
            self.vel = vec(PLAYER_SPEED / 2, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.rot = 270
            self.game.player_img = self.game.playerspritesheet.get_image(*PLAYER_IMG_NORMAL)
            self.vel = vec(PLAYER_SPEED / 2, 0).rotate(-self.rot)





    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.x = 2
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
                
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.y = 2
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y


    def update(self):
        self.get_keys()
        self.image = self.game.player_img
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        #self.rect.centerx = self.pos.x
        self.collide_with_walls('x')
        #self.rect.centery = self.pos.y
        self.collide_with_walls('y')






class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Ground(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.grass
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
