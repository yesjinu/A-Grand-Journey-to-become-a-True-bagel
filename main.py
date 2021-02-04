import time

import pygame
import sys
from Games.Table_Game import Table_sitting
from Games.Calendar_Game import Calendar
from Games.Meeting_Game import Meeting_beer
from Games.Slack_Game import Slack_pepe
from Games.Clicking_Game import Click_game
from Games.Game import Game

from Pages.Front_page import Front_page
from Pages.Ranking_page import Ranking_page
from Pages.Tutorial_page import Tutorial_page

import Input_name

from Rank_server import (get_rank, update_rank)

from pygame.locals import (
    QUIT,
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
    K_0, # front page

    K_7, # tutorial
    K_8, # start
    K_9, # ranking

    K_SPACE,
    K_RETURN,
    MOUSEBUTTONUP,
    MOUSEBUTTONDOWN
)

pygame.mixer.init()
pygame.init()
pygame.display.set_caption("A Grand Journey to become a True Bagel")

# window에 대한 정보. 일단 전체화면이 아닌 고정 윈도우로
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720 + 100
SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# clock을 초기
FPSCLOCK = pygame.time.Clock()

# font setter
FONT_60 = pygame.font.SysFont(None, 60)
FONT_24 = pygame.font.SysFont(None, 24)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

allowed_key_input = [K_SPACE, K_p, K_a, K_d, K_s, K_w, K_q, K_e, K_r, K_f, MOUSEBUTTONUP, MOUSEBUTTONDOWN]
page_key_input = [K_0, K_7, K_8, K_9]

text_input = Input_name.TextInput(initial_string="remove this line", font_size=30)
one_password_image = pygame.image.load('images/one_password.png')
type_your_name_image = pygame.image.load('images/type_your_name.png')


def main():
    # print(get_rank())
    # print(update_rank())
    # pygame은 루프문을 계속 돌면서 event(인풋)을 감지해 새로운 화면을 그린다
    game_manager = Game()
    register_all_games(game_manager)
    click_game = game_manager.game_list[-1]

    front_page = Front_page()
    tutorial_page = Tutorial_page()
    ranking_page = Ranking_page()

    page_flag = K_0
    on_game = False

    user_input_name = None
    pygame.mixer.music.load("sounds/main_page_bgm.wav")
    pygame.mixer.music.play()

    while True:

        # ranking_page_sound.play()
        while user_input_name is None:
            SURFACE.blit(one_password_image, (0, 0))
            SURFACE.blit(type_your_name_image, (150, 100))
            draw_lines_for_locate_debug()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == KEYDOWN and event.key == K_RETURN:
                    user_input_name = text_input.get_text()
                    break
            text_input.update(events)
            SURFACE.blit(text_input.get_surface(), (500, 450))

            pygame.display.update()
            FPSCLOCK.tick(30)

        user_input_name = text_input.get_text()

        # play_bgm(bgm_list, page_flag)

        # input 받는 부분
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if on_game and (event.key in allowed_key_input):
                    game_manager.detect_key_all(event.key)
                if event.key in page_key_input:
                    page_flag = event.key
            elif event.type == KEYUP:
                if event.key in allowed_key_input:
                    game_manager.update_all(event.key)
            elif event.type == MOUSEBUTTONDOWN:
                click_game.click_down_flagger()
            elif event.type == MOUSEBUTTONUP:
                click_game.update(None)
                page_flag = click_button(pygame.mouse.get_pos(), page_flag)

        # 시작 페이지
        if page_flag == K_0:
            on_game = False
            # pygame.mixer.music.stop()

            front_page.render(SURFACE)

        # 튜토리얼 페이지
        elif page_flag == K_7:
            on_game = False
            # pygame.mixer.music.stop()
            tutorial_page.render(SURFACE)

        # 게임 페이지
        elif page_flag == K_8:
            # 게임 점수 초기화를 여기에서 실행
            if not on_game:
                # print("Call only once")
                game_manager.start_games()
                on_game = True

            if game_manager.render_all(SURFACE, user_input_name):
                break

        # 랭킹 페이지
        elif page_flag == K_9:
            on_game = False
            # pygame.mixer.music.stop()
            ranking_page.render(SURFACE)

        # 윈도우에 화면 출력
        pygame.display.flip()
        FPSCLOCK.tick(30)

    print("***** MAIN CALLED *****")
    main()

def play_bgm(playing):
    if not playing:
        bgm.play()



def play_main_bgm(main_bgm, now_playing):
    if not now_playing:
        main_bgm.play()

def play_main_bgm(main_bgm, now_playing):
    if not now_playing:
        main_bgm.play()



def play_main_page_sound(m, r, t):
    m.play()
    r.stop()
    t.stop()

def play_ranking_page_sound(m, r, t):
    m.stop()
    r.play()
    t.stop()

def play_tutorial_page_sound(m, r, t):
    m.stop()
    r.stop()
    t.play()

def click_button(mouse_pos, page_flag):
    x_pos = mouse_pos[0]
    y_pos = mouse_pos[1]
    if page_flag == K_0:
        if 70 <= x_pos <= 430 and 700 <= y_pos <= 800:
            return K_7
        elif 515 <= x_pos <= 765 and 700 <= y_pos <= 800:
            return K_8
        elif 880 <= x_pos <= 1210 and 700 <= y_pos <= 800:
            return K_9
        else:
            return K_0
    elif page_flag == K_7 or page_flag == K_9:
        if 50 <= x_pos <= 150 and 50 <= y_pos <= 150:
            return K_0
        else:
            return page_flag
    elif page_flag == K_8:
        if 20 <= x_pos <= 80 and 740 <= y_pos <= 800:
            return K_0
        else:
            return K_8



def draw_lines_for_locate_debug():
    for i in range(10, 1280, 10):
        if (i % 100 == 0):
            pygame.draw.line(SURFACE, (255, 0, 0), (i, 0), (i, 820))
            continue
        if (i % 50 == 0):
            pygame.draw.line(SURFACE, BLACK, (i, 0), (i, 820))
            continue
        pygame.draw.line(SURFACE, (220,220,220), (i, 0), (i, 820))

    for i in range(10, 820, 10):
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

def get_keyboard_input_123():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key in page_key_input:
            return event.key

def get_keyboard_input_game(game_manager):
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key in allowed_key_input:
            game_manager.detect_key_all(event.key)
        elif event.type == KEYUP and event.key in allowed_key_input:
            game_manager.update_all(event.key)

def get_mouseclick_input_game(click_game):
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            click_game.click_down_flagger()
        elif event.type == MOUSEBUTTONUP:
            click_game.update(None)

def log_mouse_position():
    x, y = pygame.mouse.get_pos()
    print(x, y)

if __name__ == "__main__":
    main()