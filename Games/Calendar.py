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
        # super().add_to_game_list(self)
        self.surf = pygame.Surface((25, 50))
        self.surf.fill(BLACK)
        self.rect = Rect(640, 0, 25, 50)

        self.w_keydown_flag = False
        self.s_keydown_flag = False
        self.e_keydown_flag = False

        # 캘린더
        self.calendar_1_image = pygame.image.load('images/calendar_1.png')
        self.calendar_2_image = pygame.image.load('images/calendar_2.png')
        self.calendar_3_image = pygame.image.load('images/calendar_3.png')
        self.calendar_new_image = pygame.image.load('images/calendar_new.png')
        self.resized_calendar_1_image = pygame.transform.scale(self.calendar_1_image, (500, 300))
        self.resized_calendar_2_image = pygame.transform.scale(self.calendar_2_image, (500, 300))
        self.resized_calendar_3_image = pygame.transform.scale(self.calendar_3_image, (500, 300))
        self.resized_calendar_new_image = pygame.transform.scale(self.calendar_new_image, (143, 40))

    # Move the sprite based on user key presses
    def keydown_flagger(self, event_key):
        if event_key == K_s:
            self.s_keydown_flag = True
        elif event_key == K_w:
            self.w_keydown_flag = True
        elif event_key == K_e:
            self.e_keydown_flag = True

    def update(self, event_key):
        if event_key == K_s and self.s_keydown_flag:
            print("calendar updated")
            self.rect.move_ip(0, 100)
            self.s_keydown_flag = False
        elif event_key == K_w and self.w_keydown_flag:
            self.rect.move_ip(0, -100)
            self.w_keydown_flag = False
        elif event_key == K_e and self.e_keydown_flag:
            self.surf.fill(RED)


    def render(self, SURFACE):
        # 캘린더 게임
        SURFACE.blit(self.resized_calendar_3_image, (700, 20))
        SURFACE.blit(self.resized_calendar_new_image, (900, 40))
        SURFACE.blit(self.resized_calendar_new_image, (900, 150))
        SURFACE.blit(self.resized_calendar_new_image, (900, 260))