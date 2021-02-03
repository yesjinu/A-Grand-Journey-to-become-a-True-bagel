import pygame
import time
from pygame.locals import (
    K_p,
)
# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (229, 229, 229)

REFRESH_CYCLE = 60 * 8 / 135
il_jul = 74


# 왼쪽
# 테이블 빈 자리를 찾아가서 앉아주세요. (a, d, q)
class Game(pygame.sprite.Sprite):
    score = 10
    is_ended = False
    is_finished = False
    user_press_restart = False

    music_start_time = None
    barometer = None

    def __init__(self):
        super(Game, self).__init__()
        self.game_list = []
        self.game_over_image = pygame.image.load('images/game_over.png')
        self.game_end_popup_image = pygame.image.load('images/game_end_popup.png')

        Game.music_start_time = time.time()

    # 딱 한번만 호출
    def start_games(self):
        # 시작 시간 기록

        self.reset_class()
        # 음악 플레이 시작
        # self.game_play_music.play()
        # pygame.mixer.music.load('sounds/bad_guy.mp3') # TODO: 게임 전환 싱크 더 잘 맞추기
        # pygame.mixer.music.load('sounds/trimmed_music.mp3')
        pygame.mixer.music.load('sounds/bad_guy_sample.mp3')
        pygame.mixer.music.play()
        Game.music_start_time = time.time()
        Game.barometer = Game.music_start_time

        print(Game.music_start_time)
        print(Game.barometer)


    def add_to_game_list(self, new_game):
        self.game_list.append(new_game)

    def detect_key_all(self, event_key):
        if Game.is_ended or Game.is_finished:
            if event_key == K_p:
                print("user press restart")
                Game.user_press_restart = True
        else:
            for game in self.game_list:
                game.keydown_flagger(event_key)

    def update_all(self, event_key):
        for game in self.game_list:
            game.update(event_key)
            # TODO: 랭크서버에 접속해서 기록을 남겨야 함.

    def render_all(self, SURFACE):
        self.timer_in_bpm()
        self.is_music_ended()

        if not Game.is_ended:
            SURFACE.fill(GRAY)
            self.draw_grid_line(SURFACE)
            for game in self.game_list:
                game.render(SURFACE)
            self.score_message = pygame.font.SysFont(None, 60).render(f'Score : {self.get_score()}', False, (0, 0, 0))
            SURFACE.blit(self.score_message, (1000, 750))

        if Game.is_finished:
            SURFACE.blit(self.game_end_popup_image, (65, 0))
            print("Your score :", Game.score)
            if Game.user_press_restart:
                self.reset_class()
                return True

        if Game.is_ended:
            SURFACE.blit(self.game_over_image, (40, 0))
            if Game.user_press_restart:
                self.reset_class()
                return True

        return False
        # 전체적으로 남은 시간 표시해줘야함

    def timer_in_bpm(self):
        # print(REFRESH_CYCLE)
        now_time = time.time()
        if now_time - Game.barometer > REFRESH_CYCLE:
            self.refresh_games()
            Game.barometer = now_time

    def is_music_ended(self):
        # print(time.time(), Game.music_start_time, time.time() - Game.music_start_time)
        if time.time() - Game.music_start_time > il_jul:
            Game.is_finished = True

    def get_now_time(self):
        return time.time()

    def draw_grid_line(self, SURFACE):
        pygame.draw.line(SURFACE, BLACK, (0, 360), (1280, 360), 4) # 중간 가로줄
        pygame.draw.line(SURFACE, BLACK, (640, 0), (640, 720), 4)  # 중간 세로줄
        pygame.draw.line(SURFACE, BLACK, (0, 720), (1280, 720), 4) # 아래 가로줄

    def correct(self):
        Game.score += 10

    def wrong(self):
        Game.score -= 10
        if Game.score <= 0:
            self.end_game()

    def get_score(self):
        return self.score

    def refresh_games(self):
        for game in self.game_list:
            game.update_map()

    def end_game(self):
        Game.is_ended = True

    def reset_class(self):
        Game.is_ended = False
        Game.is_finished = False
        Game.score = 10
        Game.user_press_restart = False