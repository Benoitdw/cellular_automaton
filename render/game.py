import pygame
from src.constantes import colors, CELL_WIDTH
from src.render.matrix import Cells
from typing import Tuple



class Game:
    def __init__(self, size: Tuple[int, int]):
        pygame.init()
        self.size = size
        self.display = pygame.display.set_mode(size)
        self.display.fill(colors['BG'])
        self.cells = Cells(self.n_cells())

    def n_cells(self) -> Tuple[int, int]:
        cols, rows = self.size
        cols /= CELL_WIDTH
        rows /= CELL_WIDTH
        return int(cols),int(rows)


    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.cells.show(self.display)
        pygame.display.update()
