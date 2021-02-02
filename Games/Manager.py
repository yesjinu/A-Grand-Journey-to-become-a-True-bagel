import pygame

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


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
        for game in self.game_list:
            game.render(SURFACE)