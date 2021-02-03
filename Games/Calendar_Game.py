import pygame
from Games.Game import Game
from random import randint
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
class Calendar(Game):
    def __init__(self):
        super(Calendar, self).__init__()
        # super().add_to_game_list(self)
        # self.surf = pygame.Surface((25, 50))
        # self.surf.fill(BLACK)
        self.surf = pygame.image.load('images/calendar_new.png')
        self.rect = Rect(900, 40, 187, 52)

        self.w_keydown_flag = False
        self.s_keydown_flag = False
        self.e_keydown_flag = False

        self.is_correct = None

        # 캘린더
        self.calendar_0_image = pygame.transform.scale(pygame.image.load('images/calendar_0.png'), (500, 300))
        self.calendar_1_image = pygame.transform.scale(pygame.image.load('images/calendar_1.png'), (500, 300))
        self.calendar_2_image = pygame.transform.scale(pygame.image.load('images/calendar_2.png'), (500, 300))
        self.calendar_new_image = pygame.transform.scale(pygame.image.load('images/calendar_new.png'), (143, 40))

        self.correct_image = pygame.transform.scale(pygame.image.load('images/correct.png'), (200, 200))
        self.wrong_image = pygame.transform.scale(pygame.image.load('images/wrong.png'), (200, 200))


        # self.first_position = (640, 0)
        self.pos_idx = 0
        self.possible_place = [(900, 40), (900, 150), (900, 260)]

        self.random_picked_number = randint(0, 2)
        self.picked_map = self.load_random_map(self.random_picked_number)



    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_s:
            self.s_keydown_flag = True
        elif event_key == K_w:
            self.w_keydown_flag = True
        elif event_key == K_e:
            self.e_keydown_flag = True

    def update(self, event_key):
        if self.is_correct is None:
            if event_key == K_s and self.s_keydown_flag:
                if self.pos_idx < 2:
                    self.pos_idx += 1
                self.rect = self.possible_place[self.pos_idx]
                self.s_keydown_flag = False
            elif event_key == K_w and self.w_keydown_flag:
                if self.pos_idx > 0:
                    self.pos_idx -= 1
                self.rect = self.possible_place[self.pos_idx]
                self.w_keydown_flag = False
            elif event_key == K_e and self.e_keydown_flag:
                self.check()


    def render(self, SURFACE):
        # 캘린더 게임
        SURFACE.blit(self.picked_map, (700, 20))
        SURFACE.blit(self.surf, self.rect)
        if self.is_correct is None:
            pass # do nothing
        elif self.is_correct:
            SURFACE.blit(self.correct_image, (860, 80))
        else:
            SURFACE.blit(self.wrong_image, (860, 80))

    def load_random_map(self, random_pick):
        if random_pick == 0:
            return self.calendar_0_image
        elif random_pick == 1:
            return self.calendar_1_image
        else:
            return self.calendar_2_image

    def check(self):
        if self.pos_idx == self.random_picked_number:
            self.correct()
            self.is_correct = True
            # self.update_map()
        else:
            self.wrong()
            self.is_correct = False
        print(super().get_score())

    def update_map(self):
        while True:
            temp = randint(0, 2)
            if self.random_picked_number != temp:
                self.random_picked_number = randint(0, 2)
                break
        self.picked_map = self.load_random_map(self.random_picked_number)
        self.is_correct = None