import pygame
from Games.Game import Game
from pygame.locals import (
    Rect,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)
import time
# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

ONE_BPM = 0.44444444

# 왼쪽
# 테이블 빈 자리를 찾아가서 앉아주세요. (a, d, q)
class Click_game(Game):
    def __init__(self):
        super(Click_game, self).__init__()
        # super().add_to_game_list(self)
        self.surf = pygame.transform.scale(pygame.image.load('images/click_square.png'), (100, 100))
        self.rect = Rect(590, 310, 100, 100)

        self.mouse_down_flag = False
        self.previous_time = Game.music_start_time + ONE_BPM * 4
        self.current_time = Game.music_start_time + ONE_BPM * 4

    # Move the sprite based on user key presses
    def click_down_flagger(self):
        self.mouse_down_flag = True
        self.previous_time = self.current_time
        self.current_time = time.time()
        self.check()

    def keydown_flagger(self, event_key):
        pass

    # TODO 이미지 결과에 따라 움직임 제한할 것
    def update(self, event_key):
        if self.mouse_down_flag:
            print("click updated")
            self.mouse_down_flag = False


    def render(self, SURFACE):
        # SURFACE.blit(self.surf, self.rect)
        pass
    def check(self):
        print(self.current_time)
        print(self.get_diff())
        if self.get_diff() < 0.08:
            Game.score += 1
            print("correct")
        else:
            Game.score -= 1
            print("wrong!")


    def get_diff(self):
        return abs(self.current_time - (self.previous_time + ONE_BPM))


    def update_map(self):
        pass