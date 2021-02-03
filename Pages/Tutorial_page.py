import pygame
from enum import Enum
# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (229, 229, 229)

class Tutorial_page():
    def __init__(self):
        FONT_60 = pygame.font.SysFont(None, 60)
        self.caution_message = FONT_60.render('tutorial page', False, (50, 50, 50))

    def render(self, SURFACE):
        SURFACE.fill(GRAY)
        SURFACE.blit(self.caution_message, (0, 0))
