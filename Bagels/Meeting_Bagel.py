import random
import pygame
import sys
from pygame.locals import (
    QUIT,
    Rect,
    KEYDOWN,
    KEYUP,
    K_a,
    K_d,
    K_q,
    K_w,
    K_s,
    K_e,
    K_r,
    K_f,
    K_SPACE
)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# 게임 별로 클래스 만들어서 update 함수 다르게 하기
class Meeting_Bagel(pygame.sprite.Sprite):
    def __init__(self):
        super(Meeting_Bagel, self).__init__()
        self.surf = pygame.Surface((25, 50))
        self.surf.fill(BLACK)
        self.rect = Rect(0, 360, 25, 50)

        self.space_keydown_flag = False

    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_SPACE:
            self.space_keydown_flag = True

    def keyup_detector(self, event_key):
        if event_key == K_SPACE and self.space_keydown_flag:
            print("Meeting bagle, SPACE detected")
            self.space_keydown_flag = False