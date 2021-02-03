import pygame
from Games.Game import Game
from random import randint
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
class Table_sitting(Game):
    def __init__(self):
        super(Table_sitting, self).__init__()
        self.surf = pygame.image.load('images/table_idle_bagel.png')
        # self.rect = self.surf.get_rect() # (0, 0)을 디폴트로 받아옴
        self.rect = Rect(130, 170, 62, 106)

        self.a_keydown_flag = False
        self.d_keydown_flag = False
        self.q_keydown_flag = False

        self.is_correct = None

        self.table_people_image_1 = pygame.transform.scale(pygame.image.load('images/table_people_1.png'), (500, 150))
        self.table_people_image_2 = pygame.transform.scale(pygame.image.load('images/table_people_2.png'), (500, 150))
        self.table_people_image_3 = pygame.transform.scale(pygame.image.load('images/table_people_3.png'), (500, 150))
        self.table_people_image_4 = pygame.transform.scale(pygame.image.load('images/table_people_4.png'), (500, 150))
        self.table_idle_bagel_image = pygame.image.load('images/table_idle_bagel.png')

        self.correct_image = pygame.transform.scale(pygame.image.load('images/correct.png'), (200, 200))
        self.wrong_image = pygame.transform.scale(pygame.image.load('images/wrong.png'), (200, 200))

        # self.first_position = (20, 170)
        self.pos_idx = 0
        self.possible_place = [(130, 170), (210, 170), (290, 170), (375, 170), (455, 170)]

        self.random_picked_number = randint(1, 4)
        self.picked_map = self.load_random_map(self.random_picked_number)

    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_a:
            self.a_keydown_flag = True
        elif event_key == K_d:
            self.d_keydown_flag = True
        elif event_key == K_q:
            self.q_keydown_flag = True

    # TODO 이미지 결과에 따라 움직임 제한할 것
    def update(self, event_key):
        if self.is_correct is None:
            if event_key == K_a and self.a_keydown_flag:
                if self.pos_idx > 0:
                    self.pos_idx -= 1
                self.rect = self.possible_place[self.pos_idx]
                self.a_keydown_flag = False
            elif event_key == K_d and self.d_keydown_flag:
                if self.pos_idx < 4:
                    self.pos_idx += 1
                self.rect = self.possible_place[self.pos_idx]
                self.d_keydown_flag = False
            elif event_key == K_q and self.q_keydown_flag:
                self.check()

    def render(self, SURFACE):
        SURFACE.blit(self.picked_map, (80, 100))
        SURFACE.blit(self.surf, self.rect)
        if self.is_correct is None:
            pass # do nothing
        elif self.is_correct:
            SURFACE.blit(self.correct_image, (220, 80))
        else:
            SURFACE.blit(self.wrong_image, (220, 80))

    def load_random_map(self, random_pick):
        if random_pick == 1:
            return self.table_people_image_1
        elif random_pick == 2:
            return self.table_people_image_2
        elif random_pick == 3:
            return self.table_people_image_3
        else:
            return self.table_people_image_4

    def check(self):
        if self.pos_idx == self.random_picked_number:
            self.correct()
            self.is_correct = True
            # self.update_map()
        else:
            self.wrong()
            self.is_correct = False
        print(super().get_score())
        # print(self.pos_idx, self.random_picked_number, super().get_score())

    def update_map(self):
        self.random_picked_number = randint(1, 4)
        self.picked_map = self.load_random_map(self.random_picked_number)
        self.is_correct = None



