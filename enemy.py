import pygame
import random
from pygame.sprite import Sprite
class enemy(Sprite):
def __init__(self,enemy_image,setting):
    super(enemy,self).__init__()
    self.image = pygame.image.load('picture/')