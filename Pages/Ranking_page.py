import pygame
import Rank_server
# default color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (229, 229, 229)
class Ranking_page():
    def __init__(self):
        FONT_60 = pygame.font.SysFont(None, 60)

        self.rankers_list = Rank_server.get_rank()

        self.ranking_background_image = pygame.image.load('images/ranking_page_bg.png')
        self.ranking_nameboard_image = pygame.image.load('images/ranking_page_name_board.png')
        self.test_image = pygame.image.load('images/font_size_test.png') # TODO: Hall of Fame으로 교체할 것


        self.caution_message = FONT_60.render('ranking page', False, (50, 50, 50))
        self.ranker_1 = FONT_60.render(f'{self.rankers_list[0][0]}', False, (50, 50, 50))
        self.ranker_2 = FONT_60.render(f'{self.rankers_list[1][0]}', False, (50, 50, 50))
        self.ranker_3 = FONT_60.render(f'{self.rankers_list[2][0]}', False, (50, 50, 50))
        self.ranker_4 = FONT_60.render(f'{self.rankers_list[3][0]}', False, (50, 50, 50))
        self.ranker_5 = FONT_60.render(f'{self.rankers_list[4][0]}', False, (50, 50, 50))

        self.score_1 = FONT_60.render(f'{self.rankers_list[0][1]}', False, (50, 50, 50))
        self.score_2 = FONT_60.render(f'{self.rankers_list[1][1]}', False, (50, 50, 50))
        self.score_3 = FONT_60.render(f'{self.rankers_list[2][1]}', False, (50, 50, 50))
        self.score_4 = FONT_60.render(f'{self.rankers_list[3][1]}', False, (50, 50, 50))
        self.score_5 = FONT_60.render(f'{self.rankers_list[4][1]}', False, (50, 50, 50))




    def render(self, SURFACE):
        # SURFACE.fill(GRAY)
        SURFACE.blit(self.ranking_background_image, (0, 0))

        SURFACE.blit(self.test_image, (200, 30)) # hall of fame 이미지로 교체할 것
        SURFACE.blit(self.ranking_nameboard_image, (155, 180))

        SURFACE.blit(self.ranker_1, (350, 330))
        SURFACE.blit(self.ranker_2, (350, 420))
        SURFACE.blit(self.ranker_3, (350, 510))
        SURFACE.blit(self.ranker_4, (350, 600))
        SURFACE.blit(self.ranker_5, (350, 690))

        SURFACE.blit(self.score_1, (750, 330))
        SURFACE.blit(self.score_2, (750, 420))
        SURFACE.blit(self.score_3, (750, 510))
        SURFACE.blit(self.score_4, (750, 600))
        SURFACE.blit(self.score_5, (750, 690))
