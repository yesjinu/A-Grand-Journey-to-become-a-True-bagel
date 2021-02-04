import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT
)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (229, 229, 229)

class Tutorial_page():
    def __init__(self):
        FONT_60 = pygame.font.SysFont(None, 60)
        self.ranking_background_image = pygame.image.load('images/ranking_page_bg.png')
        self.back_icon_image = pygame.transform.scale(pygame.image.load('images/icon_back.png'), (100, 100))
        self.slide_sound = pygame.mixer.Sound('sounds/slide_sound.wav')

        self.idx = 0
        self.pic_list = []

        self.pic1 = pygame.transform.scale(pygame.image.load('images/p1.png'), (800, 700))
        self.pic2 = pygame.transform.scale(pygame.image.load('images/p2.png'), (800, 700))
        self.pic3 = pygame.transform.scale(pygame.image.load('images/p3.png'), (800, 700))
        self.pic4 = pygame.transform.scale(pygame.image.load('images/p4.png'), (800, 700))
        self.pic5 = pygame.transform.scale(pygame.image.load('images/p5.png'), (800, 700))
        self.pic6 = pygame.transform.scale(pygame.image.load('images/p6.png'), (800, 700))
        self.pic7 = pygame.transform.scale(pygame.image.load('images/p7.png'), (800, 700))
        self.pic8 = pygame.transform.scale(pygame.image.load('images/p8.png'), (800, 700))
        self.pic9 = pygame.transform.scale(pygame.image.load('images/p9.png'), (800, 700))
        self.pic10 = pygame.transform.scale(pygame.image.load('images/p10.png'), (800, 700))
        self.pic11 = pygame.transform.scale(pygame.image.load('images/p11.png'), (800, 700))
        self.pic12 = pygame.transform.scale(pygame.image.load('images/p12.png'), (800, 700))
        self.pic13 = pygame.transform.scale(pygame.image.load('images/p13.png'), (800, 700))
        self.pic14 = pygame.transform.scale(pygame.image.load('images/p14.png'), (800, 700))
        self.pic15 = pygame.transform.scale(pygame.image.load('images/p15.png'), (800, 700))
        self.pic16 = pygame.transform.scale(pygame.image.load('images/p16.png'), (800, 700))
        self.pic17 = pygame.transform.scale(pygame.image.load('images/p17.png'), (800, 700))
        self.pic18 = pygame.transform.scale(pygame.image.load('images/p18.png'), (800, 700))
        self.pic19 = pygame.transform.scale(pygame.image.load('images/p19.png'), (800, 700))
        self.pic20 = pygame.transform.scale(pygame.image.load('images/p20.png'), (800, 700))

        self.pic_list.append(self.pic1)
        self.pic_list.append(self.pic2)
        self.pic_list.append(self.pic3)
        self.pic_list.append(self.pic4)
        self.pic_list.append(self.pic5)
        self.pic_list.append(self.pic6)
        self.pic_list.append(self.pic7)
        self.pic_list.append(self.pic8)
        self.pic_list.append(self.pic9)
        self.pic_list.append(self.pic10)
        self.pic_list.append(self.pic11)
        self.pic_list.append(self.pic12)
        self.pic_list.append(self.pic13)
        self.pic_list.append(self.pic14)
        self.pic_list.append(self.pic15)
        self.pic_list.append(self.pic16)
        self.pic_list.append(self.pic17)
        self.pic_list.append(self.pic18)
        self.pic_list.append(self.pic19)
        self.pic_list.append(self.pic20)

    def render(self, SURFACE):
        SURFACE.blit(self.ranking_background_image, (0, 0))
        SURFACE.blit(self.pic_list[self.idx], (240, 50))
        SURFACE.blit(self.back_icon_image, (50, 50))


    def move_left(self):
        if self.idx > 0:
            self.slide_sound.play()
            self.idx -= 1


    def move_right(self):
        if self.idx < 19:
            self.slide_sound.play()
            self.idx += 1


