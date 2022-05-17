import pygame
import math
from pygame.locals import*
import time
import random
import sys
import json

from helpers import *
from gradient import *
from arc import *
from colors_and_images import *
from talking import *
from servernet import *

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 707

print(pygame.font.get_fonts())

SURFACE = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#SURFACE = pygame.display.set_mode((0, 0), pygame.FULLSCREE
# .N)
CLOCK = pygame.time.Clock()

SURFACE.fill((0, 100, 40))
#gradientRect_w(SURFACE, (0, 0, 10), (83, 132, 255),
                     #Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

receive()
send('connected sucsesfully')
'''
image = pygame.image.load(
    "images/WEST_logo.png").convert_alpha()
image = pygame.transform.rotozoom(image, 0, 0.98)
rect = image.get_rect()
rect.center = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40]
SURFACE.blit(image, rect)

image = pygame.image.load(
    "images/dragon_tail_sideways_gray.png").convert_alpha()
image = pygame.transform.rotozoom(image, 0, 0.0386)
rect = image.get_rect()

rect.center = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 270]
SURFACE.blit(image, rect)
'''
pygame.display.update()
time.sleep(3)

receive()
send('connected sucsesfully')

RUNNING = True

DELTA_TIME = 53
CHAT_SURF = pygame.Surface([SCREEN_WIDTH - 300, SCREEN_HEIGHT])
WRITE_SURF = pygame.Surface([SCREEN_WIDTH, 100])

while RUNNING:
    big_event = pygame.event.get()
    for event in big_event:
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                RUNNING = False

    SURFACE.fill((150, 170, 150))
    CHAT_SURF.fill((200, 200, 200))
    WRITE_SURF.fill((200, 200, 200))
    
    talk(CHAT_SURF, (0, 180, 30), big_event, SURFACE)
    SURFACE.blit(CHAT_SURF, [300, 0])

    pygame.display.update()
    CLOCK.tick(DELTA_TIME)


pygame.quit()
