import pygame
from Games.Manager import Manager
from pygame.locals import (
    Rect,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 왼쪽
# 테이블 빈 자리를 찾아가서 앉아주세요. (a, d, q)
class Click_game(Manager):
    def __init__(self):
        super(Click_game, self).__init__()
        # super().add_to_game_list(self)
        self.surf = pygame.Surface((50, 50))
        self.surf.fill(BLACK)
        self.rect = Rect(630, 350, 50, 50)

        self.mouse_down_flag = False

    # Move the sprite based on user key presses
    def click_down_flagger(self):
        self.mouse_down_flag = True

    # TODO 이미지 결과에 따라 움직임 제한할 것
    def update(self):
        if self.mouse_down_flag:
            print("click updated")
            self.mouse_down_flag = False


    def render(self, SURFACE):
        pass