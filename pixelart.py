import pygame
import math
from pygame.locals import*
import time
import random
import sys
import json

from helpers import *

pygame.init()

SURFACE = pygame.display.set_mode([1366, 707])
CLOCK = pygame.time.Clock()
FONTS = pygame.font.get_fonts()

FONT1 = pygame.font.SysFont('poorrichard', 60)

print(pygame.font.get_fonts())

SCREEN_CENTER = [SURFACE.get_width() // 2, SURFACE.get_height() // 2]

COLORS = [
    (230, 25, 75), (60, 180, 75), (255, 225, 25), (0, 130, 200), (245, 130, 48),
    (145, 30, 180), (70, 240, 240), (240, 50, 230), (210, 245, 60), (0, 200, 0),
    (250, 190, 212), (0, 128, 128), (220, 190, 255), (170, 110, 40), (150, 75, 0),
    (255, 250, 200), (128, 0, 0), (170, 255, 195), (128, 128, 0), (255, 215, 180),
    (0, 0, 128), (128, 128, 128), (200, 0,
                                   0), (255, 255, 255), (0, 0, 0), (0, 50, 15),
]


class Pixel_art(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.canvas = pygame.Surface((180, 180))
        self.gridsize = 30
        self.grid = []
        for n in range((self.canvas.get_height() // self.gridsize)):
            self.grid.append([])
            for n in range((self.canvas.get_width() // self.gridsize)):
                self.grid[len(self.grid) - 1].append((170, 170, 170))
        
        print(self.grid)

        self.brush = COLORS[0]
        self.middle = (SCREEN_CENTER[0] - 150 - (self.canvas.get_width() // 2), 
                SCREEN_CENTER[1] - self.canvas.get_height() // 2)

        self.testbutton = False

    def update(self):
        self.canvas_click()
        self.draw_canvas()

        print(self.middle)
        SURFACE.blit(self.canvas, self.middle)
        self.sidebar()

    def draw_canvas(self):
        self.canvas.fill((170, 170, 170))
        
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                pygame.draw.rect(self.canvas, self.grid[y][x], Rect(
                x * self.gridsize, y * self.gridsize, self.gridsize, self.gridsize))

        for n in range((self.canvas.get_width() // self.gridsize) + 1):
            pygame.draw.line(self.canvas, (100, 100, 100), (n * self.gridsize, 0),
                             (n * self.gridsize, self.canvas.get_height()))

        for n in range((self.canvas.get_height() // self.gridsize) + 1):
            pygame.draw.line(self.canvas, (100, 100, 100), (0, n * self.gridsize),
                             (self.canvas.get_width(), n * self.gridsize))

    def canvas_click(self):

        clicked = pygame.mouse.get_pressed()
        # print(clicked)

        x = [pygame.mouse.get_pos()[0] - self.middle[0], pygame.mouse.get_pos()[1] - self.middle[1]]

        c = (x[0] > 0 and x[0] < self.canvas.get_width()) and (
            x[1] > 0 and x[1] < self.canvas.get_height())

        if c:
            x = [x[0] - (x[0] % self.gridsize), x[1] - (x[1] % self.gridsize)]
            x = [x[0] // self.gridsize, x[1] // self.gridsize]

            if clicked[0]:
                self.grid[x[1]][x[0]] = self.brush

            if clicked[2]:
                self.grid[x[1]][x[0]] = (170, 170, 170)

    def sidebar(self):
        sidebar_width = SURFACE.get_width() - self.canvas.get_width()
        sidebar_startpos = SURFACE.get_width() - 300
        blit_text(SURFACE, (250, 250, 250), "Color",
                  (sidebar_startpos + 40, 20), FONT1)
        pygame.draw.rect(SURFACE, self.brush, Rect(
            SURFACE.get_width() - 80, 40, 40, 40))

        pygame.draw.line(SURFACE, (0, 0, 0), (sidebar_startpos +
                         30, 90), (SURFACE.get_width() - 30, 90), 5)

        save = button(SURFACE, FONT1, (200, 0, 0), 'SAVE', [sidebar_startpos + 78, 
                SURFACE.get_height() - 200], (250, 100, 0), (250, 250, 250), 0)

        if save:
            with open("info.txt", "r") as f:
               info = json.load(f)

            info["picture"] = self.grid
            
            with open("info.txt", "w") as f:
                json.dump(info, f, indent=2)
        
        load = button(SURFACE, FONT1, (200, 0, 0), 'OPEN', [sidebar_startpos + 75, 
                SURFACE.get_height() - 100], (250, 100, 0), (250, 250, 250), 0)

        if load:
            with open("info.txt", "r") as f:
               info = json.load(f)

            self.grid = info["picture"]

        x = sidebar_startpos + 35
        y = 120
        for n in COLORS:
            pygame.draw.rect(SURFACE, n, Rect(
                x, y, 40, 40))

            if detect_click_rect(0, Rect(x, y, 40, 40)):
                self.brush = n

            x += 50
            if x > SURFACE.get_width() - 50:
                y += 50
                x = sidebar_startpos + 35


running = True
DRAW = Pixel_art()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SURFACE.fill((50, 50, 50))
    #pygame.draw.line(SURFACE, (0, 150, 20), (DRAW.canvas.get_width() + 1, 0),
                     #(DRAW.canvas.get_width() + 1, SURFACE.get_width()), 5)
    
    pygame.draw.rect(SURFACE, (100, 100, 100), (1, 1, SURFACE.get_width() - 300, 
                SURFACE.get_height() - 11))
    pygame.draw.rect(SURFACE, (0, 150, 20), (1, 1, SURFACE.get_width() - 300, 
                SURFACE.get_height() - 11), 5)

    DRAW.update()

    pygame.display.update()
    CLOCK.tick(50)


pygame.quit()
