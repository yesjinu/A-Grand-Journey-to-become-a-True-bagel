import pygame
import sys
from Games.Table_sitting import Table_sitting
from Games.Calendar import Calendar
from Games.Meeting_beer import Meeting_beer
from Games.Slack_pepe import Slack_pepe
from Games.Click_rhythm import Click_game
from Games.Manager import Manager
from Front_page import Front_page
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
    K_p,
    K_SPACE,
    MOUSEBUTTONUP,
    MOUSEBUTTONDOWN
)

pygame.init()
pygame.display.set_caption("A Grand Journey to become a True Bagel")

# window에 대한 정보. 일단 전체화면이 아닌 고정 윈도우로
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# offset
#  -----------
# |  1  |  2  |
# -------------
# |  3  |  4  |
#  -----------
# FIRST_SCREEN_OFFSET = (0, 0)
# SECOND_SCREEN_OFFSET = (640, 0)
# THIRD_SCREEN_OFFSET = (0, 360)
# FOURTH_SCREEN_OFFSET = (640, 360)

# clock을 초기
FPSCLOCK = pygame.time.Clock()

# font setter
FONT_60 = pygame.font.SysFont(None, 60)
FONT_24 = pygame.font.SysFont(None, 24)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

allowed_key_input = [K_SPACE, K_a, K_d, K_s, K_w, K_q, K_e, K_r, K_f, MOUSEBUTTONUP, MOUSEBUTTONDOWN]

def main():
    # 메시지 렌더링 초기화

    on_game = False

    # pygame은 루프문을 계속 돌면서 event(인풋)을 감지해 새로운 화면을 그린다
    game_manager = Manager()
    register_all_games(game_manager)
    click_game = game_manager.game_list[-1]

    front_page = Front_page()



    while True:
        SURFACE.fill(WHITE)

        # input 받는 부분
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    on_game = True
                elif event.key in allowed_key_input:
                    game_manager.detect_key_all(event.key)
            elif event.type == KEYUP:
                if event.key in allowed_key_input:
                    game_manager.update_all(event.key)
            elif event.type == MOUSEBUTTONDOWN:
                click_game.click_down_flagger()
            elif event.type == MOUSEBUTTONUP:
                click_game.update(None)

        if not on_game: # 시작 페이지
            front_page.render(SURFACE)

        if on_game:
            game_manager.render_all(SURFACE)

        # draw_lines_for_locate_debug()
        # 윈도우에 화면 출력
        pygame.display.flip()
        FPSCLOCK.tick(30)


def align_message_center_of_screen(message):
    return ((WINDOW_WIDTH - message.get_width()) / 2, (WINDOW_HEIGHT - message.get_height()) / 2)


def show_bagel_on_screen(bagel):
    SURFACE.blit(bagel.surf, bagel.rect)

def show_message_on_screen_center(message):
    SURFACE.blit(message, align_message_center_of_screen(message))

def draw_lines_for_locate_debug():
    for i in range(10, 1280, 10):
        if (i % 100 == 0):
            pygame.draw.line(SURFACE, (255, 0, 0), (i, 0), (i, 720))
            continue
        if (i % 50 == 0):
            pygame.draw.line(SURFACE, BLACK, (i, 0), (i, 720))
            continue
        pygame.draw.line(SURFACE, (220,220,220), (i, 0), (i, 720))

    for i in range(10, 720, 10):
        if (i % 100 == 0):
            pygame.draw.line(SURFACE, (255, 0, 0), (0, i), (1280, i))
            continue
        if (i % 50 == 0):
            pygame.draw.line(SURFACE, BLACK, (0, i), (1280, i))
            continue
        pygame.draw.line(SURFACE, (220,220,220), (0, i), (1280, i))

def register_all_games(game_manager):
    table_game = Table_sitting()
    calendar_game = Calendar()
    meeting_game = Meeting_beer()
    slack_game = Slack_pepe()
    click_game = Click_game()

    game_manager.add_to_game_list(table_game)
    game_manager.add_to_game_list(calendar_game)
    game_manager.add_to_game_list(meeting_game)
    game_manager.add_to_game_list(slack_game)
    game_manager.add_to_game_list(click_game)

if __name__ == "__main__":
    main()