import pygame

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (229, 229, 229)


# 왼쪽
# 테이블 빈 자리를 찾아가서 앉아주세요. (a, d, q)
class Manager(pygame.sprite.Sprite):
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

    def draw_grid_line(self, SURFACE):
        pygame.draw.line(SURFACE, BLACK, (0, 360), (1280, 360), 4)
        pygame.draw.line(SURFACE, BLACK, (640, 0), (640, 720), 4)
