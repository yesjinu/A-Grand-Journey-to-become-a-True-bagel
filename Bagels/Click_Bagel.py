import pygame
from Bagels.Game_Common import Common
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
class Click_Bagel(Common):
    def __init__(self):
        super(Click_Bagel, self).__init__()
        self.surf = pygame.Surface((25, 50))
        self.surf.fill(BLACK)
        self.rect = Rect(640, 360, 25, 25)

        self.mouse_down_flag = False

    # Move the sprite based on user key presses
    def click_down_flagger(self):
        self.mouse_down_flag = True

    # TODO 이미지 결과에 따라 움직임 제한할 것
    def click_up_detector(self):
        if self.mouse_down_flag:
            if self.surf.get_colorkey() == BLACK:
                self.surf.fill(RED)
            else:
                self.surf.fill(BLACK)
            self.mouse_down_flag = False