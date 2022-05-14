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

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 707

print(pygame.font.get_fonts())

SURFACE = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#SURFACE = pygame.display.set_mode((0, 0), pygame.FULLSCREE
# .N)
CLOCK = pygame.time.Clock()

SURFACE.fill((200, 200, 200))
#gradientRect_w(SURFACE, (0, 0, 10), (83, 132, 255),
                     #Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
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
pygame.display.update()
time.sleep(3)


RUNNING = True

DELTA_TIME = 53

while RUNNING:
    big_event = pygame.event.get()
    for event in big_event:
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                RUNNING = False

    SURFACE.fill((200, 200, 200))
    talk(SURFACE, (0, 180, 30), big_event)
    
    pygame.display.update()
    CLOCK.tick(DELTA_TIME)


pygame.quit()
