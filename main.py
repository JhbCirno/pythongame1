import sys,random
import math
import pygame

from pygame.locals import *
from datetime import datetime,date,time
pygame.init()
a = pygame.display.set_mode((600,711))#设置窗口大小
pygame.display.set_caption('FIGHT')#给窗口建一个名称
b =int(120)#游玩时间
clock = pygame.time.Clock
space = pygame.image.load('picture/背景.jpg')#添加背景图
a.blit(space,(0,0))
pygame.display.update()
pygame.event.get()
def display():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
display()