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

        self.map = Map(path.join(game_folder, 'map.txt'))
        self.playerspritesheet = SpriteSheet(path.join(img_folder, SPRITESHEETPLAYER))
        self.worldspritesheet = SpriteSheet(path.join(img_folder, SPRITESHEETWORLD))
        self.player_img = self.playerspritesheet.get_image(*PLAYER_IMG_NORMAL)
        self.wall_img = self.worldspritesheet.get_image(*BORDER)
        self.grass = pg.image.load((path.join(img_folder, 'grass.png')))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.ground = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles.strip()):
                if tile == '.':
                    Ground(self, col, row)
                elif tile == '1':
                    Wall(self, col, row)
        self.player = Player(self, 2, 2)
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
        self.screen.fill(BGCOLOR)
        #self.img = self.grass
        self.draw_grid()
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
                    #self.player_img = self.spritesheet.get_image(*PLAYER_IMG_LEFT)
                    #print("No")
                    pass
                if event.key == pg.K_ESCAPE:
                    self.quit()
            
                
                




    def show_start_screen(self):
        pass


    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
