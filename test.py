import pygame
import time
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('snd/walk.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(100)