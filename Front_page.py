import pygame

class Front_page():
    def __init__(self):
        self.main_title_image = pygame.image.load('images/main_title.png')
        self.bagelcode_logo_image = pygame.image.load('images/bagelcode_logo.png')
        self.resized_main_title_image = pygame.transform.scale(self.main_title_image, (1100, 395))
        self.resized_bagelcode_logo_image = pygame.transform.scale(self.bagelcode_logo_image, (100, 100))

    def render(self, SURFACE):
        SURFACE.blit(self.resized_main_title_image, (90, 70))
        SURFACE.blit(self.resized_bagelcode_logo_image, (590, 540))
