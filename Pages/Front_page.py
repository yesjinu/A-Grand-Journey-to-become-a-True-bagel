import pygame
from enum import Enum

class Front_page():
    def __init__(self):
        # self.main_title_image = pygame.image.load('images/main_title.png')
        self.main_title_image = pygame.image.load('images/main_title_image.png')
        # self.bagelcode_logo_image = pygame.transform.scale(pygame.image.load('images/bagelcode_logo.png')
        # self.resized_bagelcode_logo_image = pygame.transform.scale(self.bagelcode_logo_image, (100, 100))
        FONT_24 = pygame.font.SysFont(None, 24)
        self.caution_message = FONT_24.render('This game does NOT support various window size cause it\'s hard-coded. '
                                              'Thank you for reading my excuses. You\'re so nice. Good luck.', False, (50, 50, 50))

        self.button_start_image = pygame.transform.scale(pygame.image.load('images/button_start.png'), (250, 100))
        self.button_tutorial_image = pygame.transform.scale(pygame.image.load('images/button_tutorial.png'), (358, 100))
        self.button_ranking_image = pygame.transform.scale(pygame.image.load('images/button_ranking.png'), (332, 100))


    def render(self, SURFACE):
        SURFACE.blit(self.main_title_image, (0, 0))
        SURFACE.blit(self.caution_message, (0, 0))
        SURFACE.blit(self.button_tutorial_image, (70, 700))
        SURFACE.blit(self.button_start_image, (515, 700))
        SURFACE.blit(self.button_ranking_image, (878, 700))
        # SURFACE.blit(self.resized_bagelcode_logo_image, (590, 540))
