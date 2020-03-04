import pygame
import pytmx
from pytmx.util_pygame import load_pygame

# initialize pygame
pygame.init()
clock = pygame.time.Clock() 

# create game display
game_display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Collision detection with Tiled and pytmx")
red = pygame.Color(153,0,0)
pytmx_map = load_pygame("img/FirstMap.tmx") 


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       self.rect = self.image.get_rect()

       self.movement_dict = {'left': (-2,0), 'right': (2,0), 'down': (0,2), 'up': (0,-2), 'rest': (0,0)}
       self.movement = 'rest'

    def update(self, event):
        if event != None:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_LEFT:
                    self.movement = 'left'
                elif event.key == pygame.K_RIGHT:
                    self.movement = 'right'
                elif event.key == pygame.K_DOWN:
                    self.movement = 'down'
                elif event.key == pygame.K_UP:
                    self.movement = 'up'
            elif event.type == pygame.KEYUP:
                self.movement = 'rest'

        self.rect.x += self.movement_dict[self.movement][0]
        self.rect.y += self.movement_dict[self.movement][1]

    def draw(self, display):
        display.blit(self.image, self.rect)


block = Block(red, 32, 32)
background = pygame.Surface((25*32, 25*32))
loop = True
event = None
while(loop):
    for event in pygame.event.get():
        pass

    layer_index = 0
    for layer in pytmx_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x in range(0, 25):
                for y in range(0, 25):
                    image = pytmx_map.get_tile_image(x, y, layer_index)
                    if image != None:
                        image = pygame.transform.scale(image, (40, 40))
                        background.blit(image, (40*x, 40*y))
        layer_index += 1
        if isinstance(layer, pytmx.TiledObjectGroup):
            #if layer.name == "hit block":
            for obj in layer:
                #print('Obj:', obj.x, obj.y)
                wall = pygame.Rect(obj.x*2.5, obj.y*2.5, obj.width, obj.height)
                wall = pygame.transform.scale(wall, (40, 40))
                if wall.colliderect(block.rect) == True:
                
                    print ("YOU HIT THE RED BLOCK!!")
                else:
                    print(0)
                    

    block.update(event)
    game_display.blit(background, (0,0))
    block.draw(game_display)
    clock.tick(60)
    pygame.display.update()