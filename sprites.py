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
        image = pg.transform.scale(image, ((width*2, height*2)))
        image.set_colorkey((WHITE))
        return image

    def loadImage(self, inimage, x, y, width, height):
        #Gets image off sprite sheet
        image = pg.Surface((width, height))
        image.blit(inimage, (0,0), (x, y, width, height))
        image = pg.transform.scale(image, ((width*2, height*2)))
        image.set_colorkey((WHITE))
        return image
    
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.last_update = pg.time.get_ticks()
        self.frame = 0
        self.frame_rate = ANIMATIONSPEED
        self.direction = 'down'

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.game.walk_sound.play(-1)
            now = pg.time.get_ticks()
            self.vx = -200
            self.direction = 'left'
            if now - self.last_update > self.frame_rate:
               self.last_update = now
               try:
                    self.game.player_img = self.game.walkleft[self.frame]
                    self.frame += 1
               except IndexError:
                    self.frame = 0
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.game.walk_sound.play(-1)
            now = pg.time.get_ticks()
            self.vx = 200
            self.direction = 'right'
            if now - self.last_update > self.frame_rate:
               self.last_update = now
               try:
                    self.game.player_img = self.game.walkright[self.frame]
                    self.frame += 1
               except IndexError:
                    self.frame = 0
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.game.walk_sound.play(-1)
            now = pg.time.get_ticks()
            self.vy = -200
            self.direction = 'up'
            if now - self.last_update > self.frame_rate:
               self.last_update = now
               try:
                    self.game.player_img = self.game.walkup[self.frame]
                    self.frame += 1
               except IndexError:
                    self.frame = 0
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            
            self.game.walk_sound.play(-1)
            now = pg.time.get_ticks()
            self.direction = 'down'
            self.vy = 200
            if now - self.last_update > self.frame_rate:
               self.last_update = now
               try:
                    self.game.player_img = self.game.walkdown[self.frame]
                    self.frame += 1
               except IndexError:
                    self.frame = 0
        elif keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            try:
                if now - self.last_update > self.frame_rate:
                    if self.direction == 'down':
                        self.game.player_img = self.game.playerattackdown[self.frame]
                        self.frame += 1
                        self.last_update = now
                    if self.direction == 'up':
                        self.game.player_img = self.game.playerattackup[self.frame]
                        self.frame += 1
                        self.last_update = now
                    if self.direction == 'left':
                        self.game.player_img = self.game.playerattackleft[self.frame]
                        self.frame += 1
                        self.last_update = now
                    if self.direction == 'right':
                        self.game.player_img = self.game.playerattackright[self.frame]
                        self.frame += 1
                        self.last_update = now
            except IndexError:
                self.frame = 0
        elif self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
        elif keys[pg.K_t]:
            self.x = 1 * TILESIZE
            self.y = 1 * TILESIZE
        else:
            self.game.walk_sound.stop()
            if self.direction == 'down':
                self.game.player_img = self.game.walkdown[1]
            if self.direction == 'up':
                self.game.player_img = self.game.walkup[1]
            if self.direction == 'right':
                self.game.player_img = self.game.walkright[1]
            if self.direction == 'left':
                self.game.player_img = self.game.walkleft[1]

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
        
        hits = pg.sprite.spritecollide(self, self.game.swords, True)
        if hits:
            self.game.show_go_screen()
       

    def update(self):
        self.get_keys()
        self.image = self.game.player_img
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        print(self.game.gamemap)





class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Ground(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.ground
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.grass
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Sword(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.swords
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.sword
        self.image.set_colorkey(WHITE)
        self.image = pg.transform.scale(self.image, (TILESIZE+50, TILESIZE-0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
