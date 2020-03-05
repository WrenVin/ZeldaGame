import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
from pytmx import TiledObjectGroup
from platform import system


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        #pg.key.set_repeat(1, 20)
        self.font_name = pg.font.match_font(FONT_NAME)
        self.gamemap = 'img/FirstMap.tmx'
        #self.load_data()
        


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
        self.player_img = self.playerspritesheet.get_image(*PLAYER_IMG_NORMAL).convert()
        #self.wall_img = self.map.get_tile_image(0, 5, 0)
        #self.grass = self.map.get_tile_image(0, 0, 0)
        self.sword = pg.image.load((path.join(img_folder, 'sword.png'))).convert()
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
        self.attackdown1 = self.playerspritesheet.get_image(*ATTACKDOWN1).convert()
        self.attackdown2 = self.playerspritesheet.get_image(*ATTACKDOWN2).convert()
        self.attackdown3 = self.playerspritesheet.get_image(*ATTACKDOWN3).convert()
        self.attackdown4 = self.playerspritesheet.get_image(*ATTACKDOWN4).convert()
        self.playerattackdown = [self.attackdown1, self.attackdown2, self.attackdown3, self.attackdown4, self.walkdown1]
        self.attackup1 = self.playerspritesheet.get_image(*ATTACKUP1).convert()
        self.attackup2 = self.playerspritesheet.get_image(*ATTACKUP2).convert()
        self.attackup3 = self.playerspritesheet.get_image(*ATTACKUP3).convert()
        self.attackup4 = self.playerspritesheet.get_image(*ATTACKUP4).convert()
        self.playerattackup = [self.attackup1, self.attackup2, self.attackup3, self.attackup4, self.walkup1]
        self.attackleft1 = self.playerspritesheet.get_image(*ATTACKLEFT1).convert()
        self.attackleft2 = self.playerspritesheet.get_image(*ATTACKLEFT2).convert()
        self.attackleft3 = self.playerspritesheet.get_image(*ATTACKLEFT3).convert()
        self.attackleft4 = self.playerspritesheet.get_image(*ATTACKLEFT4).convert()
        self.playerattackleft = [self.attackleft1, self.attackleft2, self.attackleft3, self.attackleft4, self.walkleft1]
        self.attackright1 = self.playerspritesheet.get_image(*ATTACKRIGHT1).convert()
        self.attackright2 = self.playerspritesheet.get_image(*ATTACKRIGHT2).convert()
        self.attackright3 = self.playerspritesheet.get_image(*ATTACKRIGHT3).convert()
        self.attackright4 = self.playerspritesheet.get_image(*ATTACKRIGHT4).convert()
        self.playerattackright = [self.attackright1, self.attackright2, self.attackright3, self.attackright4, self.walkright1]
        
    def new(self):
        self.load_data()
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.ground = pg.sprite.Group()
        #self.swords = pg.sprite.Group()
        layer_index = 0
        for layer in self.map.txmdata.visible_layers:
            if isinstance(layer, TiledTileLayer):
                if layer.name == "PlayerLayer":
                    self.player = Player(self, 4, 4)
                for i in range(self.map.txmdata.height):
                    for b in range(self.map.txmdata.width):
                        if self.map.txmdata.get_tile_image(b, i, layer_index):
                            #print(self.map.txmdata.get_tile_image(b, i, x),b, i, x)
                            MapTile(self, b, i, self.map.txmdata.get_tile_image(b, i,layer_index))
            layer_index += 1

            if isinstance(layer, TiledObjectGroup):
                for obj in layer:
                    Obstacle(self, obj.x, obj.y, obj.width, obj.height)
        #self.player = Player(self, 8, 8)
        self.camera = Camera(self.map.width, self.map.height)
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.screen.fill(BLACK)
        self.player.update()
        self.camera.update(self.player)

    def draw(self):
        #self.screen.fill(BGCOLOR)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.update()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.VIDEORESIZE:
                self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                
       # if len(self.swords) == 0:
          #  self.playing = False
        
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
        waiting = True
        while waiting:
            keys = pg.key.get_pressed()
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.playing = False
            if keys[pg.K_1]:
                self.gamemap = 'FirstMap.tmx'
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
    #g.show_go_screen()
