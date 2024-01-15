import sys
import pygame
import time
import random
import os
from levels import *
from sprites import *
from config import *


pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("囧 go_away")
pygame.display.set_icon(pygame.image.load(you_image))
clock = pygame.time.Clock()

time_start = None
time_elapsed = None


def draw_screen():
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()


draw_walls()
draw_screen()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            pygame.quit()
            sys.exit()

    clock.tick(update_time)

    all_sprites.update()
    draw_screen()
