import pygame
import numpy as np
from pygame.gfxdraw import box
from utils import colors, CELL_WIDTH, color_ids
from cellular_automaton.src.matrix import Cells, Cell
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
        for matrix in self.cells:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            render(self.display, matrix)
            pygame.display.update()


def render(display: pygame.display, matrix: np.array):
    for x in range(matrix.shape[1]):
        for y in range(matrix.shape[0]):
            cell = Cell(CELL_WIDTH, (x, y), color_ids[matrix[x][y] + 1])
            box(display, (cell.position, cell.shape), cell.color)