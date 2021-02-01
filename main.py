import random
import math
import pygame
import sys
from Bagel import Table_Bagel
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
WINDOW_HEIGHT = 720
SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# offset
#  -----------
# |  1  |  2  |
# -------------
# |  3  |  4  |
#  -----------d
FIRST_SCREEN_OFFSET = (0, 0)
SECOND_SCREEN_OFFSET = (640, 0)
THIRD_SCREEN_OFFSET = (0, 360)
FOURTH_SCREEN_OFFSET = (640, 360)

# clock을 초기
FPSCLOCK = pygame.time.Clock()

# font setter
FONT_60 = pygame.font.SysFont(None, 60)
FONT_24 = pygame.font.SysFont(None, 24)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    # 메시지 렌더링 초기화
    main_title_message = FONT_60.render("A Grand Journey to become a True Bagel", True, BLACK)

    game_started = False
    allowed_key_input = [K_SPACE, K_a, K_d, K_s, K_w, K_q, K_e, K_r, K_f]

    # pygame은 루프문을 계속 돌면서 event(인풋)을 감지해 새로운 화면을 그린다
    bagel = Table_Bagel()

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

        if not game_started:
            SURFACE.blit(main_title_message, get_center_of_message(main_title_message))

        if game_started:
            draw_grid_line()
            SURFACE.blit(bagel.surf, bagel.rect)


        # 윈도우에 화면 출력
        pygame.display.flip()
        FPSCLOCK.tick(30)


def get_center_of_message(message):
    return ((WINDOW_WIDTH - message.get_width()) / 2, (WINDOW_HEIGHT - message.get_height()) / 2)

def draw_grid_line():
    pygame.draw.line(SURFACE, BLACK, (0, 360), (1280, 360))
    pygame.draw.line(SURFACE, BLACK, (640, 0), (640, 720))

if __name__ == "__main__":
    main()