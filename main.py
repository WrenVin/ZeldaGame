import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        #pg.key.set_repeat(1, 20)
        self.load_data()


    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')   
        self.map = Map(path.join(game_folder, GAMEMAP))
        self.playerspritesheet = SpriteSheet(path.join(img_folder, SPRITESHEETPLAYER))
        self.worldspritesheet = SpriteSheet(path.join(img_folder, SPRITESHEETWORLD))
        self.player_img = self.playerspritesheet.get_image(*PLAYER_IMG_NORMAL).convert()
        self.wall_img = self.worldspritesheet.get_image(*BORDER).convert()
        self.grass = pg.image.load((path.join(img_folder, 'grass.png'))).convert()
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
        
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.ground = pg.sprite.Group()
        self.swords = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles.strip()):
                if tile == '+' or tile == '-' or tile == '|':
                    Wall(self, col, row)
                elif tile == ' ':
                    Ground(self, col, row)
                elif tile == 'A':
                    Ground(self, col, row)
                    Sword(self, col-0.5, row)
                
        self.player = Player(self, 1, 1)
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
        self.player.update()
        self.camera.update(self.player)
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        #self.screen.fill(BGCOLOR)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    pass
                if event.key == pg.K_ESCAPE:
                    self.quit()
        if len(self.swords) == 0:
            self.playing = False
        
            

    def show_start_screen(self):
        pass


    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
