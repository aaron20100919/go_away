import sys
import pygame
import time
import random
import os
from pygame.locals import *
from config import *


def clear_callback(surf, rect):
    surf.fill(bg_color, rect)


class You(pygame.sprite.Sprite):
    def __init__(self):
        super(You, self).__init__()
        self.image = pygame.image.load(you_image)
        self.image = pygame.transform.scale(
            self.image, (box_size[0] - 1, box_size[1] - 1)
        )
        self.rect = self.image.get_rect()
        self.velocity_x = 0
        self.velocity_y = 0
        self.rect.bottomleft = 0, screen_size[1]
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.velocity_x = 0

        if keys[K_a]:
            self.velocity_x = -velocity_x
        if keys[K_d]:
            self.velocity_x = velocity_x
        if keys[K_a] and keys[K_d]:
            self.velocity_x = 0
        if keys[K_SPACE]:
            if self.velocity_x:
                self.velocity_x = self.velocity_x / velocity_x
        if keys[K_r]:
            self.rect.bottomleft = 0, screen_size[1]

        self.rect.x += self.velocity_x

        if self.on_ground:
            if keys[K_w]:
                self.velocity_y = -velocity_y
                self.on_ground = False

        self.velocity_y += g
        self.rect.y += self.velocity_y

        wall_collision = pygame.sprite.spritecollide(self, walls, False)

        for wall in wall_collision:
            if abs(wall.rect.right - self.rect.left) <= abs(self.velocity_x):
                self.rect.left = wall.rect.right
                self.velocity_x = 0
            if abs(wall.rect.left - self.rect.right) <= abs(self.velocity_x):
                self.rect.right = wall.rect.left
                self.velocity_x = 0

            intersection_rect = self.rect.clip(wall)
            intersection_area = intersection_rect.width * intersection_rect.height

            if intersection_area <= min_intersection:
                continue

            if abs(wall.rect.top - self.rect.bottom) <= abs(self.velocity_y) + 1:
                self.rect.bottom = wall.rect.top
                self.velocity_y = 0
                self.on_ground = True
            if abs(wall.rect.bottom - self.rect.top) <= abs(self.velocity_y) + 1:
                self.rect.top = wall.rect.bottom
                self.velocity_y = 0

        # for wall in wall_collision:
        #     if self.rect.bottom <= wall.rect.bottom < self.rect.top:
        #         if self.velocity_x > 0:
        #             if self.rect.right > wall.rect.left:
        #                 self.rect.right = wall.rect.left
        #         elif self.velocity_x < 0:
        #             if self.rect.left < wall.rect.right:
        #                 self.rect.left = wall.rect.right
        #         continue

        #     if self.velocity_y == 0:
        #         if self.rect.bottom <= wall.rect.bottom < self.rect.top:
        #             continue

        #     if self.velocity_y == 0:
        #         if wall.rect.bottom <= self.rect.bottom < wall.rect.top:
        #             continue

        #     if self.velocity_y > 0:
        #         if self.rect.bottom > wall.rect.top:
        #             self.rect.bottom = wall.rect.top
        #             self.velocity_y = 0
        #             self.on_ground = True

        #     if self.velocity_y < 0:
        #         if self.rect.top < wall.rect.bottom:
        #             self.rect.top = wall.rect.bottom
        #             self.velocity_y = 0
        #             self.on_ground = False

        if self.rect.bottom > screen_size[1]:
            self.rect.bottom = screen_size[1]
            self.velocity_y = 0
            self.on_ground = True

        if self.rect.right > screen_size[0]:
            self.rect.right = screen_size[0]
            self.velocity_x = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity_x = 0


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Wall, self).__init__()
        self.image = pygame.image.load(wall_image)
        self.image = pygame.transform.scale(self.image, box_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y


class Flag(pygame.sprite.Sprite):
    def __init__(self):
        super(Flag, self).__init__()
        self.image = pygame.image.load(flag_image)
        self.image = pygame.transform.scale(self.image, box_size)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.right = screen_size[0]

    def update(self):
        global time_start, time_elapsed

        if pygame.sprite.spritecollide(self, [you], False, pygame.sprite.collide_rect):
            time_elapsed = round(time.time() - time_start, 2)
            print(f"You win!!! Time taken: {time_elapsed} seconds")
            time.sleep(2)
            pygame.quit()
            sys.exit()


all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()


you = You()
all_sprites.add(you)
flag = Flag()
all_sprites.add(flag)
