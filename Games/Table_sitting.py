import pygame
from Games.Manager import Manager
from pygame.locals import (
    Rect,
    K_a,
    K_d,
    K_q,
)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 왼쪽
# 테이블 빈 자리를 찾아가서 앉아주세요. (a, d, q)
class Table_sitting(Manager):
    def __init__(self):
        super(Table_sitting, self).__init__()
        super().add_to_game_list(self)
        self.surf = pygame.Surface((25, 50))
        self.surf.fill(BLACK)
        self.rect = Rect(0, 0, 25, 50)

        self.a_keydown_flag = False
        self.d_keydown_flag = False
        self.q_keydown_flag = False

    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_a:
            self.a_keydown_flag = True
        elif event_key == K_d:
            self.d_keydown_flag = True
        elif event_key == K_q:
            self.q_keydown_flag = True

    # TODO 이미지 결과에 따라 움직임 제한할 것
    def keyup_detector(self, event_key):
        if event_key == K_a and self.a_keydown_flag:
            self.rect.move_ip(-100, 0)
            self.a_keydown_flag = False
        elif event_key == K_d and self.d_keydown_flag:
            self.rect.move_ip(100, 0)
            self.d_keydown_flag = False
        elif event_key == K_q and self.q_keydown_flag:
            self.surf.fill(RED)