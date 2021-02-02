import pygame

class Front_page():
    def __init__(self):
        # self.main_title_image = pygame.image.load('images/main_title.png')
        self.main_title_image = pygame.image.load('images/main_title_image.png')
        # self.bagelcode_logo_image = pygame.transform.scale(pygame.image.load('images/bagelcode_logo.png')
        # self.resized_bagelcode_logo_image = pygame.transform.scale(self.bagelcode_logo_image, (100, 100))
        FONT_24 = pygame.font.SysFont(None, 24)
        self.caution_message = FONT_24.render('This game does NOT support various window size cause it\'s hard-coded. '
                                              'Thank you for reading this tiny message. You\'re so nice. Good luck.', False, (255, 255, 255))

    def render(self, SURFACE):
        SURFACE.blit(self.main_title_image, (0, 0))
        SURFACE.blit(self.caution_message, (0, 0))
        # SURFACE.blit(self.resized_bagelcode_logo_image, (590, 540))
