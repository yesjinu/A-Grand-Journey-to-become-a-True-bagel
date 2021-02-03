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


    def add_to_game_list(self, new_game):
        self.game_list.append(new_game)

    def detect_key_all(self, event_key):
        for game in self.game_list:
            game.keydown_flagger(event_key)

    def update_all(self, event_key):
        for game in self.game_list:
            game.update(event_key)

    def render_all(self, SURFACE):
        SURFACE.fill(GRAY)
        self.draw_grid_line(SURFACE)
        for game in self.game_list:
            game.render(SURFACE)
        FONT_60 = pygame.font.SysFont(None, 60)
        self.score_message = FONT_60.render(f'Score : {self.get_score()}', False, (255, 255, 255))
        SURFACE.blit(self.score_message, (640, 720))

    def refresh_all_games(self):
        for game in self.game_list:
            game.update_map()


    def draw_grid_line(self, SURFACE):
        pygame.draw.line(SURFACE, BLACK, (0, 360), (1280, 360), 4) # 중간 가로줄
        pygame.draw.line(SURFACE, BLACK, (640, 0), (640, 720), 4)  # 중간 세로줄
        pygame.draw.line(SURFACE, BLACK, (0, 720), (1280, 720), 4) # 아래 가로줄

    def correct(self):
        Manager.score += 10

    def wrong(self):
        Manager.score -= 10
        if Manager.score == 0:
            pass # you lose

    def get_score(self):
        return self.score
