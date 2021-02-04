import pygame
import time
import Input_name
import Rank_server
from pygame.locals import (
    K_0,
)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (229, 229, 229)
GLOW_RED = (255, 204, 204)

ONE_BPM = 60 / 135
il_jul = 76


# 왼쪽
# 테이블 빈 자리를 찾아가서 앉아주세요. (a, d, q)
class Game(pygame.sprite.Sprite):
    score = 10
    is_ended = False
    is_finished = False
    user_press_restart = False
    REFRESH_CYCLE = 60 * 8 / 135

    music_start_time = None
    barometer = None

    textinput = Input_name.TextInput(font_size=60)

    def __init__(self):
        super(Game, self).__init__()
        self.game_list = []
        self.game_over_image = pygame.image.load('images/game_over.png')
        self.game_end_popup_image = pygame.image.load('images/game_end_popup.png')
        self.back_icon_image = pygame.transform.scale(pygame.image.load('images/icon_back.png'), (60, 60))


        Game.music_start_time = time.time()
        self.next_bpm = Game.music_start_time + ONE_BPM
        self.stamp_sound = pygame.mixer.Sound('sounds/stamp_sound.wav')




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
        # bad_guy = pygame.mixer.Sound('sounds/bad_guy_sample.mp3')
        # bad_guy.play()
        Game.music_start_time = time.time()
        Game.barometer = Game.music_start_time

        print(Game.music_start_time)
        print(Game.barometer)


    def add_to_game_list(self, new_game):
        self.game_list.append(new_game)

    def detect_key_all(self, event_key):
        if Game.is_ended or Game.is_finished:
            # Game.user_press_restart = True
            if event_key == K_0:
                print("user press restart")
                Game.user_press_restart = True
        else:
            for game in self.game_list:
                game.keydown_flagger(event_key)

    def update_all(self, event_key):
        for game in self.game_list:
            game.update(event_key)
            # TODO: 랭크서버에 접속해서 기록을 남겨야 함.

    def render_all(self, SURFACE, user_name):
        self.timer_in_bpm()
        self.is_music_ended()
        self.getting_harder_refresh_cycle()
        print(Game.REFRESH_CYCLE)

        if not Game.is_ended:
            SURFACE.fill(GRAY)
            self.draw_alternate_grid_line(SURFACE)
            for game in self.game_list:
                game.render(SURFACE)
            self.score_message = pygame.font.SysFont(None, 60).render(f'Score : {self.get_score()}', False, (0, 0, 0))
            SURFACE.blit(self.score_message, (1000, 750))
            SURFACE.blit(self.back_icon_image, (20, 740))

        if Game.is_finished:
            SURFACE.blit(self.game_end_popup_image, (65, 0))
            # Type your name:
            # Your score is 000
            # Press '0'to restart
            Rank_server.update_rank(user_name, Game.score)
            print("your name : ", user_name)
            print("Your score :", Game.score)
            # 잘 들어가는 것 확인, 이미지만 넣으면 됨.
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
        if now_time - Game.barometer > Game.REFRESH_CYCLE:
            self.refresh_games()
            Game.barometer = now_time

    def is_music_ended(self):
        # print(time.time(), Game.music_start_time, time.time() - Game.music_start_time)
        if time.time() - Game.music_start_time > il_jul:
        # if time.time() - Game.music_start_time > 5:
            Game.is_finished = True

    def get_now_time(self):
        return time.time()

    def correct(self):
        Game.score += 10
        self.stamp_sound.play()

    def wrong(self):
        Game.score -= 10
        self.stamp_sound.play()
        if Game.score <= 0:
            self.end_game() # 게임 끝나는 용 사운드 추가할 것!!!!!!!!!!!

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
        Game.textinput = Input_name.TextInput(font_size=60)

    def getting_harder_refresh_cycle(self):
        if time.time() < Game.music_start_time + 43:
            pass
        elif time.time() < Game.music_start_time + 60:
            Game.REFRESH_CYCLE = 60 * 4 / 135
        else:
            Game.REFRESH_CYCLE = 60 * 2 / 135




    def draw_alternate_grid_line(self, SURFACE):
        curr_time = time.time()
        if self.next_bpm < curr_time:
            self.draw_glow_grid_line(SURFACE)
            self.next_bpm = curr_time + ONE_BPM
        else:
            self.draw_black_grid_line(SURFACE)

    def draw_black_grid_line(self, SURFACE):
        pygame.draw.line(SURFACE, BLACK, (0, 360), (1280, 360), 4) # 중간 가로줄
        pygame.draw.line(SURFACE, BLACK, (640, 0), (640, 720), 4)  # 중간 세로줄
        pygame.draw.line(SURFACE, BLACK, (0, 720), (1280, 720), 4) # 아래 가로줄

    def draw_glow_grid_line(self, SURFACE):
        pygame.draw.line(SURFACE, GLOW_RED, (0, 360), (1280, 360), 4)  # 중간 가로줄
        pygame.draw.line(SURFACE, GLOW_RED, (640, 0), (640, 720), 4)  # 중간 세로줄
        pygame.draw.line(SURFACE, BLACK, (0, 720), (1280, 720), 4) # 아래 가로줄
