import pygame
import sys
from Games.Table_sitting import Table_sitting
from Games.Calendar import Calendar
from Games.Meeting_beer import Meeting_beer
from Games.Slack_pepe import Slack_pepe
from Games.Click_rhythm import Click_game
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
    main_title_message = FONT_60.render("A Grand Journey to become a True Bagel", True, BLACK)

    table_people_image = pygame.image.load('images/table_people_2.png')
    resized_table_people_image = pygame.transform.scale(table_people_image, (500, 150))
    table_run_bagel_1_image = pygame.image.load('images/table_run_bagel_1.png')
    table_run_bagel_2_image = pygame.image.load('images/table_run_bagel_2.png')
    table_idle_bagel_image = pygame.image.load('images/table_idle_bagel.png')

    monitor_black_image = pygame.image.load('images/monitor.png')
    resized_monitor_black_image = pygame.transform.scale(monitor_black_image, (384, 300))
    monitor_logo_image = pygame.image.load('images/monitor_logo_bagelcode.png')
    monitor_idle_bagel_image = pygame.image.load('images/monitor_idle_bagel.png')
    monitor_beer_bagel_image = pygame.image.load('images/monitor_beer_bagel.png')
    monitor_front_image = pygame.image.load('images/monitor_front.png')
    monitor_side_image = pygame.image.load('images/monitor_side.png')

    calendar_1_image = pygame.image.load('images/calendar_1.png')
    calendar_2_image = pygame.image.load('images/calendar_2.png')
    calendar_3_image = pygame.image.load('images/calendar_3.png')
    resized_calendar_1_image = pygame.transform.scale(calendar_1_image, (500, 300))
    resized_calendar_2_image = pygame.transform.scale(calendar_2_image, (500, 300))
    resized_calendar_3_image = pygame.transform.scale(calendar_3_image, (500, 300))
    calendar_new_image = pygame.image.load('images/calendar_new.png')
    resized_calendar_new_image = pygame.transform.scale(calendar_new_image, (143, 40))

    slack_good_image = pygame.image.load('images/slack_good_kpi.png')
    slack_bad_image = pygame.image.load('images/slack_bad_kpi.png')
    resized_slack_good_image = pygame.transform.scale(slack_good_image, (500, 300))
    resized_slack_bad_image = pygame.transform.scale(slack_bad_image, (500, 300))

    slack_pepe_good_image = pygame.image.load('images/slack_pepe_good.png')
    slack_pepe_mad_image = pygame.image.load('images/slack_pepe_mad.png')
    resized_slack_pepe_good_image = pygame.transform.scale(slack_pepe_good_image, (100, 100))
    resized_slack_pepe_mad_image = pygame.transform.scale(slack_pepe_mad_image, (100, 100))




    on_game = False

    # pygame은 루프문을 계속 돌면서 event(인풋)을 감지해 새로운 화면을 그린다
    table_game = Table_sitting()
    calendar_game = Calendar()
    meeting_game = Meeting_beer()
    slack_game = Slack_pepe()
    click_game = Click_game()


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
                    table_game.keydown_flagger(event.key)
                    calendar_game.keydown_flagger(event.key)
                    meeting_game.keydown_flagger(event.key)
                    slack_game.keydown_flagger(event.key)
            elif event.type == KEYUP:
                if event.key in allowed_key_input:
                    table_game.keyup_detector(event.key)
                    calendar_game.keyup_detector(event.key)
                    meeting_game.keyup_detector(event.key)
                    slack_game.keyup_detector(event.key)

            elif event.type == MOUSEBUTTONDOWN:
                click_game.click_down_flagger()
            elif event.type == MOUSEBUTTONUP:
                click_game.click_up_detector()

        if not on_game: # 시작 페이지
            show_message_on_screen_center(main_title_message)

        if on_game:
            draw_grid_line()

            show_bagel_on_screen(table_game)
            show_bagel_on_screen(calendar_game)
            show_bagel_on_screen(meeting_game)
            show_bagel_on_screen(slack_game)
            # show_bagel_on_screen(click_game)

            # 테이블 게임
            SURFACE.blit(resized_table_people_image, (80, 100))
            SURFACE.blit(table_idle_bagel_image, (20, 170))
            SURFACE.blit(table_idle_bagel_image, (130, 170))
            SURFACE.blit(table_idle_bagel_image, (210, 170))
            SURFACE.blit(table_idle_bagel_image, (290, 170))
            SURFACE.blit(table_idle_bagel_image, (375, 170))
            SURFACE.blit(table_idle_bagel_image, (455, 170))

            # 모니터 게임
            SURFACE.blit(resized_monitor_black_image, (200, 400))
            SURFACE.blit(monitor_beer_bagel_image, (50, 510))

            # 캘린더 게임
            SURFACE.blit(resized_calendar_3_image, (700, 20))
            SURFACE.blit(resized_calendar_new_image, (900, 40))
            SURFACE.blit(resized_calendar_new_image, (900, 150))
            SURFACE.blit(resized_calendar_new_image, (900, 260))

            # 슬랙 게임
            SURFACE.blit(resized_slack_good_image, (700, 400))
            SURFACE.blit(resized_slack_pepe_good_image, (1000, 570))

            # draw_lines_for_locate_debug()




        # 윈도우에 화면 출력
        pygame.display.flip()
        FPSCLOCK.tick(30)


def align_message_center_of_screen(message):
    return ((WINDOW_WIDTH - message.get_width()) / 2, (WINDOW_HEIGHT - message.get_height()) / 2)

def draw_grid_line():
    pygame.draw.line(SURFACE, BLACK, (0, 360), (1280, 360), 4)
    pygame.draw.line(SURFACE, BLACK, (640, 0), (640, 720), 4)

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


if __name__ == "__main__":
    main()