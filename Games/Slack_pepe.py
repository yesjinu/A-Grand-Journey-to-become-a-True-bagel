import pygame
from random import randint
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
        # super().add_to_game_list(self)
        # self.surf = pygame.Surface((25, 50))
        # self.surf.fill(BLACK)
        # 비어있는 rect를 만들어놓고 거기에 그림을 박기
        self.surf = pygame.transform.scale(pygame.image.load('images/slack_pepe_calm.png'), (100, 100))
        self.rect = Rect(1000, 570, 100, 100)

        self.r_keydown_flag = False
        self.f_keydown_flag = False

        # 슬랙
        self.slack_good_image = pygame.image.load('images/slack_good_kpi.png')
        self.slack_bad_image = pygame.image.load('images/slack_bad_kpi.png')
        self.slack_pepe_good_image = pygame.image.load('images/slack_pepe_good.png')
        self.slack_pepe_mad_image = pygame.image.load('images/slack_pepe_mad.png')
        self.resized_slack_pepe_good_image = pygame.transform.scale(self.slack_pepe_good_image, (100, 100))
        self.resized_slack_pepe_mad_image = pygame.transform.scale(self.slack_pepe_mad_image, (100, 100))
        self.resized_slack_good_kpi_image = pygame.transform.scale(self.slack_good_image, (500, 300))
        self.resized_slack_bad_kpi_image = pygame.transform.scale(self.slack_bad_image, (500, 300))

    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_r:
            self.r_keydown_flag = True
        elif event_key == K_f:
            self.f_keydown_flag = True

    # TODO : r, f에 따라 적절한 이미지를 삽입
    def update(self, event_key):
        if event_key == K_r and self.r_keydown_flag:
            self.surf = self.resized_slack_pepe_good_image
            self.r_keydown_flag = False
        elif event_key == K_f and self.f_keydown_flag:
            self.surf = self.resized_slack_pepe_mad_image
            self.f_keydown_flag = False

    def render(self, SURFACE):
        # 슬랙 게임
        SURFACE.blit(self.resized_slack_good_kpi_image, (700, 400))
        SURFACE.blit(self.surf, self.rect)

        # SURFACE.blit(self.resized_slack_pepe_good_image, (1000, 570))

    def load_random_image(self):
        random_pick = randint(0, 1)
        if random_pick == 0:
            return pygame.image.load('images/slack_good_kpi.png')
        else:
            return pygame.image.load('images/slack_bad_kpi.png')