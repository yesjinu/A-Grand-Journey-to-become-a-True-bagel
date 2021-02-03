import pygame
from Games.Manager import Manager
from random import randint
from pygame.locals import (
    Rect,
    K_SPACE
)
import time

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 왼쪽 아래
# 대표님이 고개를 돌릴 때 스페이스바를 눌러 맥주를 마시세요
class Meeting_beer(Manager):
    def __init__(self):
        super(Meeting_beer, self).__init__()
        self.surf = pygame.image.load('images/monitor_idle_bagel.png')
        # self.surf = pygame.Surface((25, 50))
        # self.surf.fill(BLACK)
        self.rect = Rect(50, 510, 103, 160)

        self.space_keydown_flag = False
        self.drink = False

        # 모니터
        self.monitor_black_image = pygame.transform.scale(pygame.image.load('images/monitor.png'), (384, 300))
        # self.monitor_beer_bagel_image = pygame.image.load('images/monitor_beer_bagel.png')

        self.monitor_front_both = pygame.transform.scale(pygame.image.load('images/monitor_front_both.png'), (340, 215))
        self.monitor_front_one1 = pygame.transform.scale(pygame.image.load('images/monitor_front_11.png'), (340, 215))
        self.monitor_front_one2 = pygame.transform.scale(pygame.image.load('images/monitor_front_11.png'), (340, 215))
        self.monitor_side_both = pygame.transform.scale(pygame.image.load('images/monitor_side_both.png'), (340, 215))

        self.random_picked_number = randint(0, 3)
        self.picked_map = self.load_random_map(self.random_picked_number)

        # drink한 시간
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0


    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_SPACE:
            if self.start_time is None:
                self.start_time = time.time()
            self.surf = pygame.image.load('images/monitor_beer_bagel.png')
            self.space_keydown_flag = True
            # self.check() # 시간에 따라 점수를 주는 체계 필요함.

    def update(self, event_key):
        if event_key == K_SPACE and self.space_keydown_flag:
            self.check()
            self.surf = pygame.image.load('images/monitor_idle_bagel.png')
            # self.drink = True
            self.space_keydown_flag = False

    def render(self, SURFACE):
        # 모니터 게임
        SURFACE.blit(self.monitor_black_image, (200, 400))
        SURFACE.blit(self.picked_map, (221, 420))
        SURFACE.blit(self.surf, self.rect)

    def load_random_map(self, random_pick):
        if random_pick == 0:
            return self.monitor_front_both
        elif random_pick == 1:
            return self.monitor_front_one1
        elif random_pick == 2:
            return self.monitor_front_one2
        else:
            return self.monitor_side_both

    def check(self):
        self.elapsed_time += (time.time() - self.start_time)
        self.start_time = None
        if self.space_keydown_flag:
            self.start_time = time.time()

        print(self.elapsed_time)
        if self.random_picked_number == 3:
            correct_time = int(self.elapsed_time)
            for i in range(correct_time):
                self.correct()
            self.elapsed_time = 0
        else:
            wrong_time = int(self.elapsed_time)
            for i in range(wrong_time):
                self.wrong()
            self.elapsed_time = 0

    def update_map(self):
        self.update(None)
        self.random_picked_number = randint(0, 3)
        self.picked_map = self.load_random_map(self.random_picked_number)


