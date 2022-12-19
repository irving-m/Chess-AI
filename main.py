import pygame
import sys

from const import *
from game import Game

class Main():

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Chess")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game = Game()

    def main_loop(self):

        game = self.game
        screen = self.screen

        while True:
            game.show_bg(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
        

main = Main()
main.main_loop()
