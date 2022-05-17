import math
import random
import sys
import pygame
from pygame.locals import *
import time
import json

from helpers import *
from arc import *
from designs import *
from colors_and_images import *
from servernet import *

pygame.init()

FONT1 = pygame.font.SysFont('consolas', 30)
FONT2 = pygame.font.SysFont('consolas', 30)

TALK_WORD = ""
TALK_CHAT = []
TALK_WORD_Y = 40
SEARCH = False
SCROLL = 50

def talk(surface, theme_color, big_event, non_scrolling_surf):
    global TALK_WORD
    global TALK_CHAT
    global TALK_WORD_Y
    global SEARCH 
    global SCROLL
    
    pos = Rect(460, surface.get_height() - 15 -
               TALK_WORD_Y, 510, TALK_WORD_Y)
    pygame.draw.rect(surface, theme_color, pos, 2, 20)

    if check_released(-3):
        SEARCH = mouse_in_rect(pos, [300, 0])

    if pygame.time.get_ticks() % 100 == 1:
        recived = receive()
        #print(recived)
        for n in recived:
            q = textbox(surface, n,
                        480, [-1000, -1000], FONT1, theme_color)
                        
            hihi = [q[0], 480]

            TALK_CHAT.insert(0, [n, hihi, 6, 1])

    y = SCROLL

    if SEARCH:
        for event in big_event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and TALK_WORD != "":
                    '''
                    print('"', TALK_WORD, '"')
                    q = textbox(surface, TALK_WORD,
                                480, [-1000, -1000], FONT1, theme_color)
                        
                    hihi = [q[0], 480]
                    print(q, 'gfgfgfgfdgfdgfdgfgdfgfdg')

                    TALK_CHAT.insert(0, [TALK_WORD, hihi, 6, 0])
                    TALK_CHAT.insert(0, [TALK_WORD, hihi, 6, 1])
                    print(TALK_CHAT)
                    TALK_WORD = ""
                    '''
                    send(TALK_WORD)
                    TALK_WORD = ""
                elif event.key == pygame.K_BACKSPACE:
                    TALK_WORD = TALK_WORD[:-1]
                else:
                    TALK_WORD += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: 
                    SCROLL -= 15
                if event.button == 5: 
                    SCROLL += 15


        #print('"', TALK_WORD, '"')
        a = textbox(surface, TALK_WORD, 485, [465, surface.get_height() - 15 - TALK_WORD_Y + 5],
                    FONT1, (80, 80, 80))

        if pygame.time.get_ticks() % 1000 > 500:
            pygame.draw.line(surface, edit_colors(
                theme_color, (0.5, 0.5, 0.5)), (a[1][0] + 2, a[1][1] + 3), (a[1][0] + 2, a[1][1] + 26), 2)

        TALK_WORD_Y = a[0] + 10
        y += a[0] + 10

    else:
        blit_text(surface, (100, 100, 100), "Talk", [pos.midleft[0] + 50, pos.midleft[1]], FONT2, 1)
        y += 40

    index = 0
    for n in TALK_CHAT:
        hihi = n[1]
        if n[3] == 0:
            c = theme_color
            x = 390
        else:
            c = (150, 150, 150)
            x = 110
            #blit_pixelart(surface, [40, surface.get_height() - hihi[0] - y], 7)
        
        pygame.draw.rect(surface, c,
                         ((x, surface.get_height() - hihi[0] - y), (hihi[1], hihi[0] + 14)), 0, 20)

        textbox(surface, n[0], 490, [
                x, surface.get_height() - hihi[0] - y + 6], FONT1, (80, 80, 80))
        index += 1
        y += hihi[0] + 30
    
    scroll_line(surface, (0, 180, 30), surface.get_width() -
                20, y - SCROLL - 50, surface.get_height() - 99, -SCROLL, surface.get_height() - 99, -1)

def textbox(surface, text, max_width, pos, font, color):
    a = text.split(" ")
    startx = pos[0]
    starty = pos[1]
    maximum = startx + max_width
    for n in a:
        pos[0] += 10
        b = font.render(n, True, color)

        assert max_width > b.get_width() + 10
        # always has to be true

        if pos[0] + b.get_width() > maximum:
            pos[0] = startx + 10
            pos[1] += 40

        surface.blit(b, pos)
        pos[0] += b.get_width()

    return [(pos[1] + b.get_height()) - starty, pos]

