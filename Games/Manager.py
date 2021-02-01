import pygame
from pygame.locals import (
    Rect,
)
from abc import ABC

# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# 왼쪽
# 테이블 빈 자리를 찾아가서 앉아주세요. (a, d, q)
class Manager(pygame.sprite.Sprite):
    def __init__(self):
        super(Manager, self).__init__()

    def click_down_flagger(self):
        pass

    # TODO 이미지 결과에 따라 움직임 제한할 것
    def click_up_detector(self):
        pass

    def update(self):
        pass

    def render(self):
        pass