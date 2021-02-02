import pygame
from Games.Manager import Manager
from pygame.locals import (
    Rect,
    K_SPACE
)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 왼쪽 아래
# 대표님이 고개를 돌릴 때 스페이스바를 눌러 맥주를 마시세요
class Meeting_beer(Manager):
    def __init__(self):
        super(Meeting_beer, self).__init__()
        # super().add_to_game_list(self)
        self.surf = pygame.Surface((25, 50))
        self.surf.fill(BLACK)
        self.rect = Rect(0, 360, 25, 50)

        self.space_keydown_flag = False

        # 모니터
        self.monitor_black_image = pygame.image.load('images/monitor.png')
        self.monitor_beer_bagel_image = pygame.image.load('images/monitor_beer_bagel.png')
        self.resized_monitor_black_image = pygame.transform.scale(self.monitor_black_image, (384, 300))

    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_SPACE:
            self.space_keydown_flag = True

    def update(self, event_key):
        if event_key == K_SPACE and self.space_keydown_flag:
            print("meeting updated")
            print("Meeting bagle, SPACE detected")
            self.space_keydown_flag = False

    def render(self, SURFACE):
        # 모니터 게임
        SURFACE.blit(self.resized_monitor_black_image, (200, 400))
        SURFACE.blit(self.monitor_beer_bagel_image, (50, 510))
