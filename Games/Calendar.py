import pygame
from Games.Manager import Manager
from pygame.locals import (
    Rect,
    K_w,
    K_s,
    K_e,
)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 오른쪽 위
# 캘린더에서 s(아래)로, w(위)로, e(확정)로 빈 시간에 일정을 넣어주세요.
class Calendar(Manager):
    def __init__(self):
        super(Calendar, self).__init__()
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
