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
class Calendar_Bagel(pygame.sprite.Sprite):
    def __init__(self):
        super(Calendar_Bagel, self).__init__()
        self.surf = pygame.Surface((25, 50))
        self.surf.fill(BLACK)
        self.rect = Rect(640, 0, 25, 50)

        self.w_keydown_flag = False
        self.s_keydown_flag = False
        self.e_keydown_flag = False

    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_s:
            self.s_keydown_flag = True
        elif event_key == K_w:
            self.w_keydown_flag = True
        elif event_key == K_e:
            self.e_keydown_flag = True

    def keyup_detector(self, event_key):
        if event_key == K_s and self.s_keydown_flag:
            self.rect.move_ip(0, 100)
            self.s_keydown_flag = False
        elif event_key == K_w and self.w_keydown_flag:
            self.rect.move_ip(0, -100)
            self.w_keydown_flag = False
        elif event_key == K_e and self.e_keydown_flag:
            self.surf.fill(RED)
