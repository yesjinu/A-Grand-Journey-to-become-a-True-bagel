import pygame
from Games.Manager import Manager
from pygame.locals import (
    Rect,
    K_r,
    K_f,
)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 오른쪽 아
# Daily revenue가 증가하면 r을 눌러 pepe_ddabong을 감소하면 f를 눌러 pepe_sad를 날려주세요
class Slack_pepe(Manager):
    def __init__(self):
        super(Slack_pepe, self).__init__()
        super().add_to_game_list(self)
        self.surf = pygame.Surface((25, 50))
        self.surf.fill(BLACK)
        self.rect = Rect(640, 360, 25, 50)

        self.r_keydown_flag = False
        self.f_keydown_flag = False

    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_r:
            self.r_keydown_flag = True
        elif event_key == K_f:
            self.f_keydown_flag = True

    # TODO : r, f에 따라 적절한 이미지를 삽입
    def keyup_detector(self, event_key):
        if event_key == K_r and self.r_keydown_flag:
            print("Slack bagel, r detected")
            self.r_keydown_flag = False
        elif event_key == K_f and self.f_keydown_flag:
            print("Slack bagel, f detected")
            self.f_keydown_flag = False
