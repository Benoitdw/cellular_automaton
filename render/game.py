import pygame
from cellular_automaton.constantes import colors
from cellular_automaton.render.cells import Cells
from typing import Tuple


class Game:
    def __init__(self, size: Tuple):
        pygame.init()
        self.size = size
        self.display = pygame.display.set_mode(size)
        self.display.fill(colors['BG'])
        self.cells = Cells((10, 10))

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.cells.show(self.display)
        pygame.display.update()
