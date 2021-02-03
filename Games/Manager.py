import pygame
import time
# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (229, 229, 229)


# 왼쪽
# 테이블 빈 자리를 찾아가서 앉아주세요. (a, d, q)
class Manager(pygame.sprite.Sprite):
    score = 100
    def __init__(self):
        super(Manager, self).__init__()
        self.game_list = []
        self.game_start_time = None
        self.barometer = None




    def add_to_game_list(self, new_game):
        self.game_list.append(new_game)

    def detect_key_all(self, event_key):
        for game in self.game_list:
            game.keydown_flagger(event_key)

    def update_all(self, event_key):
        for game in self.game_list:
            game.update(event_key)

    def render_all(self, SURFACE):
        self.timer_3sec()

        SURFACE.fill(GRAY)
        self.draw_grid_line(SURFACE)
        for game in self.game_list:
            game.render(SURFACE)
        FONT_60 = pygame.font.SysFont(None, 60)
        self.score_message = FONT_60.render(f'Score : {self.get_score()}', False, (255, 255, 255))
        SURFACE.blit(self.score_message, (640, 720))

        # print(self.get_score())
        # 일정 시간이 지날 때마다 모니터 게임을 리프레시 해줘야 함

        # 전체적으로 남은 시간 표시해줘야함

    def timer_3sec(self):
        if self.get_now_time() - self.barometer > 5:
            self.refresh_games()
            self.barometer = self.get_now_time()

    def draw_grid_line(self, SURFACE):
        pygame.draw.line(SURFACE, BLACK, (0, 360), (1280, 360), 4) # 중간 가로줄
        pygame.draw.line(SURFACE, BLACK, (640, 0), (640, 720), 4)  # 중간 세로줄
        pygame.draw.line(SURFACE, BLACK, (0, 720), (1280, 720), 4) # 아래 가로줄

    def correct(self):
        Manager.score += 10

    def wrong(self):
        Manager.score -= 10
        if Manager.score == 0:
            self.end_game()

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 100

    def get_now_time(self):
        return time.time()


    # 딱 한번만 호출
    def start_games(self):
        # 시작 시간 기록
        self.game_start_time = self.get_now_time()
        self.barometer = self.game_start_time

        # 음악 플레이 시작

    def refresh_games(self):
        for game in self.game_list:
            game.update_map()

    def end_game(self):
        # 점수 초기화
        # self.reset_score()
        self.score = 100
        # 더이상 클릭 안 되게 해야 함
        # 다시 플레이할 수 있는 버튼이 있어야 함. -> start_games 호출
        pass
