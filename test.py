import pygame
import sys
from pygame.locals import QUIT

pygame.init()
Surface = pygame.display.set_mode((1200, 600))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Test Window")


def main():
    while True:
        Surface.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 빨간 가로 선
        pygame.draw.line(Surface, (255, 0, 0), (30, 30), (150, 30))
        pygame.draw.line(Surface, (255, 0, 0), (30, 70), (150, 70), 8)
        pygame.draw.line(Surface, (255, 0, 0), (30, 140), (150, 140), 15)

        # 파란 세로 선
        pygame.draw.line(Surface, (0, 0, 255), (230, 10), (230, 150))
        pygame.draw.line(Surface, (0, 0, 255), (270, 10), (270, 150), 8)
        pygame.draw.line(Surface, (0, 0, 255), (330, 10), (330, 150), 15)

        #녹색 빗금 선
        start = [(30,250),(30,300),(30,350)]
        end = [(390,300),(390,350),(390,390)]
        pygame.draw.line(Surface, (0, 255, 0), start[0], end[0], 5)
        pygame.draw.line(Surface, (0, 255, 0), start[1], end[1], 5)
        pygame.draw.line(Surface, (0, 255, 0), start[2], end[2], 5)

        pygame.display.update()
        FPSCLOCK.tick(30)






if __name__ == '__main__':
    main()