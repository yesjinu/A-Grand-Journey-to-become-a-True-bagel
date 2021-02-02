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
        self.slack_good_kpi_image = pygame.transform.scale(pygame.image.load('images/slack_good_kpi.png'), (500, 300))
        self.slack_bad_kpi_image = pygame.transform.scale(pygame.image.load('images/slack_bad_kpi.png'), (500, 300))
        self.slack_pepe_good_image = pygame.transform.scale(pygame.image.load('images/slack_pepe_good.png'), (100, 100))
        self.slack_pepe_mad_image = pygame.transform.scale(pygame.image.load('images/slack_pepe_mad.png'), (100, 100))

        self.random_picked_number = randint(0, 1)
        self.picked_map = self.load_random_map(self.random_picked_number)

    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_r:
            self.r_keydown_flag = True
        elif event_key == K_f:
            self.f_keydown_flag = True

    # TODO : r, f에 따라 적절한 이미지를 삽입
    def update(self, event_key):
        if event_key == K_r and self.r_keydown_flag:
            self.surf = self.slack_pepe_good_image
            self.r_keydown_flag = False
            self.check()
        elif event_key == K_f and self.f_keydown_flag:
            self.surf = self.slack_pepe_mad_image
            self.f_keydown_flag = False
            self.check()

    def render(self, SURFACE):
        # 슬랙 게임
        SURFACE.blit(self.picked_map, (700, 400))
        SURFACE.blit(self.surf, self.rect)

    def load_random_map(self, random_pick):
        if random_pick == 0:
            return self.slack_good_kpi_image
        else:
            return self.slack_bad_kpi_image

    def check(self):
        if (self.random_picked_number == 0 and self.surf == self.slack_pepe_good_image) or \
                (self.random_picked_number == 1 and self.surf == self.slack_pepe_mad_image):
            self.correct()
        else:
            self.wrong()
        print(super().get_score())
