import random
import math
import pygame
import sys
import Bagel
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

pygame.init()
pygame.display.set_caption("A Grand Journey to become a True Bagel")
# pygame.key.set_repeat(15, 15)

# window에 대한 정보. 일단 전체화면이 아닌 고정 윈도우로
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 760
SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# offset
#  -----------
# |  1  |  2  |
# -------------
# |  3  |  4  |
#  -----------d
SECOND_SCREEN_OFFSET = (640, 0)
THIRD_SCREEN_OFFSET = (0, 380)
FOURTH_SCREEN_OFFSET = (640, 380)

# clock을 초기
FPSCLOCK = pygame.time.Clock()

# font setter
FONT_60 = pygame.font.SysFont(None, 60)
FONT_24 = pygame.font.SysFont(None, 24)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 게임 별로 클래스 만들어서 update 함수 다르게 하기
class Bagel(pygame.sprite.Sprite):
    def __init__(self):
        super(Bagel, self).__init__()
        self.surf = pygame.Surface((25, 50))
        self.surf.fill(BLACK)
        self.rect = self.surf.get_rect()

        self.space_keydown_flag = False
        self.a_keydown_flag = False
        self.d_keydown_flag = False
        self.s_keydown_flag = False
        self.w_keydown_flag = False

    # Move the sprite based on user keypresses
    def keydown_flagger(self, event_key):
        if event_key == K_w:
            self.w_keydown_flag = True
        elif event_key == K_s:
            self.s_keydown_flag = True
        elif event_key == K_a:
            self.a_keydown_flag = True
        elif event_key == K_d:
            self.d_keydown_flag = True

    def keyup_detector(self, event_key):
        print(event_key == K_a)
        print(event_key == K_d)
        print(event_key == K_s)
        print(event_key == K_w)
        if event_key == K_a and self.a_keydown_flag:
            self.rect.move_ip(-10, 0)
            self.a_keydown_flag = False
        elif event_key == K_d and self.d_keydown_flag:
            self.rect.move_ip(10, 0)
            self.d_keydown_flag = False
        elif event_key == K_w and self.w_keydown_flag:
            self.rect.move_ip(0, -10)
            self.w_keydown_flag = False
        elif event_key == K_s and self.s_keydown_flag:
            self.rect.move_ip(0, 10)
            self.s_keydown_flag = False

def main():
    # 메시지 렌더링 초기화
    main_title_message = FONT_60.render("A Grand Journey to become a True Bagel", True, BLACK)
    # start_message = FONT_24.render("PRESS SPACE BAR", True, BLACK)

    game_started = False
    space_keydown_flag = False
    allowed_key_input = [K_SPACE, K_a, K_d, K_s, K_w]

    # pygame은 루프문을 계속 돌면서 event(인풋)을 감지해 새로운 화면을 그린다
    bagel = Bagel()

    while True:
        SURFACE.fill(WHITE)
        # 마우스, 키보드 클릭 이벤트를 계속 listen
        for event in pygame.event.get():
            # TODO: 나중에는 event.type에 따라 index를 변화시키고, index에 따라 다른 창으로 이동하는 로직을 사용할 것
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 이때 동작하게 만들
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game_started = True
                elif event.key in allowed_key_input:
                    bagel.keydown_flagger(event.key)

            elif event.type == KEYUP:
                if event.key in allowed_key_input:
                    bagel.keyup_detector(event.key)
                # elif event.key == K_a and a_keydown_flag:
                #     bagel.rect.move_ip(-100, 0)
                #     a_keydown_flag = False
                # elif event.key == K_d and d_keydown_flag:
                #     bagel.rect.move_ip(100, 0)
                #     d_keydown_flag = False
                # elif event.key == K_w and w_keydown_flag:
                #     bagel.rect.move_ip(0, -100)d
                #     w_keydown_flag = False
                # elif event.key == K_s and s_keydown_flag:
                #     bagel.rect.move_ip(0, 100)
                #     s_keydown_flag = False
                    print(event.key)


        if not game_started:
            SURFACE.blit(main_title_message, get_center_of_message(main_title_message))
            # SURFACE.blit(start_message, get_center_of_message(start_message))

        # if game_started:
        #     pressed_keys = pygame.key.get_pressed()
        #     released_keys = pygame.key.get_released()
        #     bagel.update(pressed_keys)
        #     bagel.update(released_keys)

        SURFACE.blit(bagel.surf, bagel.rect)


        # 윈도우에 화면 출력
        pygame.display.flip()
        FPSCLOCK.tick(30)


def get_center_of_message(message):
    return ((WINDOW_WIDTH - message.get_width()) / 2, (WINDOW_HEIGHT - message.get_height()) / 2)

if __name__ == "__main__":
    main()