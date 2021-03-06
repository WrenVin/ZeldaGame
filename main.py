import pygame as pg
from os import path
from settings import *
from sprites import *
from tilemap import *
from pytmx import TiledObjectGroup
from platform import system
from sys import exit
from pygame.locals import *

class Game:
    def __init__(self):
        pg.init()
        flags = FULLSCREEN | DOUBLEBUF
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), flags)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.gamemap = 'img/FirstMap.tmx'
        self.attack = False
        pg.mouse.set_visible(False)
        


    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        snd_folder = path.join(game_folder, 'snd')
        if system() != 'Darwin':
            pg.mixer.music.load(path.join(snd_folder, 'background.mp3'))
            pg.mixer.music.set_volume(0.15)
            pg.mixer.music.play(-1, 0) 
        self.walk_sound = pg.mixer.Sound('snd/walk.mp3')
        self.victory_sound = pg.mixer.Sound('snd/victory.mp3')
        self.walk_sound.set_volume(0.03)
        self.victory_sound.set_volume(0.5) 
        self.map = Map(path.join(img_folder, self.gamemap))
        self.playerspritesheet = SpriteSheet(path.join(img_folder, SPRITESHEETPLAYER))
        self.worldspritesheet = SpriteSheet(path.join(img_folder, SPRITESHEETWORLD))
        self.swordspritesheet = SpriteSheet(path.join(img_folder, 'sword.png'))
        self.player_img = self.playerspritesheet.get_image(*PLAYER_IMG_NORMAL).convert()
        self.woodensword = self.swordspritesheet.get_image(*WOODEN_SWORD).convert()
        self.metalsword = self.swordspritesheet.get_image(*METAL_SWORD).convert()
        self.epicsword = self.swordspritesheet.get_image(*EPIC_SWORD).convert()
        self.walkdown1 = self.playerspritesheet.get_image(*WALKDOWN1).convert()
        self.walkdown2 = self.playerspritesheet.get_image(*WALKDOWN2).convert()
        self.walkdown3 = self.playerspritesheet.get_image(*WALKDOWN3).convert()
        self.walkdown4 = self.playerspritesheet.get_image(*WALKDOWN4).convert()
        self.walkdown = [self.walkdown1, self.walkdown2, self.walkdown3, self.walkdown4]
        self.walkright1 = self.playerspritesheet.get_image(*WALKRIGHT1).convert()
        self.walkright2 = self.playerspritesheet.get_image(*WALKRIGHT2).convert()
        self.walkright3 = self.playerspritesheet.get_image(*WALKRIGHT3).convert()
        self.walkright4 = self.playerspritesheet.get_image(*WALKRIGHT4).convert()
        self.walkright = [self.walkright1, self.walkright2, self.walkright3, self.walkright4]
        self.walkleft1 = self.playerspritesheet.get_image(*WALKLEFT1).convert()
        self.walkleft2 = self.playerspritesheet.get_image(*WALKLEFT2).convert()
        self.walkleft3 = self.playerspritesheet.get_image(*WALKLEFT3).convert()
        self.walkleft4 = self.playerspritesheet.get_image(*WALKLEFT4).convert()
        self.walkleft = [self.walkleft1, self.walkleft2, self.walkleft3, self.walkleft4]
        self.walkup1 = self.playerspritesheet.get_image(*WALKUP1).convert()
        self.walkup2 = self.playerspritesheet.get_image(*WALKUP2).convert()
        self.walkup3 = self.playerspritesheet.get_image(*WALKUP3).convert()
        self.walkup4 = self.playerspritesheet.get_image(*WALKUP4).convert()
        self.walkup = [self.walkup1, self.walkup2, self.walkup3, self.walkup4]
        self.attackdown4 = self.playerspritesheet.get_image(*ATTACKDOWN4).convert()
        self.attackleft2 = self.playerspritesheet.get_image(*ATTACKLEFT2).convert()
        self.attackright2 = self.playerspritesheet.get_image(*ATTACKRIGHT2).convert()
        
    def new(self):
        self.load_data()
        self.sword = self.woodensword
        self.cursor = pg.transform.rotate(self.sword, 135)
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.ground = pg.sprite.Group()
        self.swords = pg.sprite.Group()
        layer_index = 0
        for layer in self.map.txmdata.visible_layers:
            if isinstance(layer, TiledTileLayer):
                if layer.name == "PlayerLayer":
                    self.player = Player(self, 4, 4)
                for i in range(self.map.txmdata.height):
                    for b in range(self.map.txmdata.width):
                        if self.map.txmdata.get_tile_image(b, i, layer_index):
                            MapTile(self, b, i, self.map.txmdata.get_tile_image(b, i,layer_index))
            layer_index += 1
            if isinstance(layer, TiledObjectGroup):
                for obj in layer:
                    Obstacle(self, obj.x, obj.y, obj.width, obj.height)
        self.camera = Camera(self.map.width, self.map.height)
        
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        exit()

    def update(self):
        self.player.update()
        self.camera.update(self.player)
        print(self.clock.get_fps())

    def draw(self):
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.screen.blit(self.cursor, pg.mouse.get_pos())
        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not self.attack:
                    self.attack = True
                    if self.player.direction == 'down':
                        self.playersword = Sword(self, self.player.rect.centerx+2, self.player.rect.bottom-11, self.player, -90)
                        self.player_img = self.attackdown4
                    if self.player.direction == 'left':
                        self.playersword = Sword(self, self.player.rect.x-27, self.player.rect.y+20, self.player, -180)
                        self.player_img = self.attackleft2
                    if self.player.direction == 'up':
                        self.playersword = Sword(self, self.player.rect.centerx-9, self.player.rect.top-26, self.player, -270)
                        self.player_img = self.walkup2 
                    if self.player.direction == 'right':
                        self.playersword = Sword(self, self.player.rect.right-6, self.player.rect.centery-2, self.player, -0)
                        self.player_img = self.attackright2
                    if  pg.sprite.spritecollide(self.playersword, self.walls, False):
                        self.playersword.kill()
                        self.attack = False
                if event.key == pg.K_5:
                    self.sword = self.metalsword
                if event.key == pg.K_4:
                    self.sword = self.woodensword
                if event.key == pg.K_6:
                    self.sword = self.epicsword
            if event.type == pg.KEYUP and self.attack:
                if event.key == pg.K_SPACE:
                    self.playersword.kill()
                    self.attack = False
        
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (int(x), int(y))
        self.screen.blit(text_surface, text_rect)        

    def show_start_screen(self):
        self.screen.fill(GREEN)
        self.draw_text("Trial of the Sword", 30, WHITE, WIDTH/2, HEIGHT/3)
        self.draw_text("Search the maze for the sword in the stone!", 20, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press 1 for easy, 2 for moderate, 3 for hard.", 20, WHITE, WIDTH/2, HEIGHT* 3/4)
        pg.display.flip()
        self.wait_for_key()
        
    def wait_for_key(self):
        self.gamemap = 'FirstMap.tmx'
        waiting = False
        while waiting:
            keys = pg.key.get_pressed()
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.playing = False
            if keys[pg.K_1]:
                pass
                waiting = False
            if keys[pg.K_2]:
                self.gamemap = 'ModerateMap.txt'
                waiting = False
            if keys[pg.K_3]:
                self.gamemap = 'HardMap.txt'
                waiting = False
                           
    def show_go_screen(self):
        if system() != 'Darwin':
            pg.mixer.music.fadeout(2000)
            pg.mixer.music.stop()
        self.walk_sound.stop()
        self.walk_sound.stop()
        self.screen.fill(ORANGE)
        self.draw_text("You found the Sword!!", 36, WHITE, WIDTH/2, HEIGHT/3)
        self.draw_text("Play again!", 20, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press 1 for moderate, 2 for hard, 3 for inasane.", 20, WHITE, WIDTH/2, HEIGHT* 3/4)
        pg.display.flip()
        self.victory_sound.play()
        self.wait_for_key()
        
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
