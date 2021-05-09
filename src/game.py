import pygame
import numpy as np
from pygame.gfxdraw import box, vline, hline
from utils import colors, CELL_WIDTH, color_ids, SPEED, NB_STATE
from cellular_automaton.src.matrix import Cells, Cell
from typing import Tuple
from time import sleep


class Game:
    def __init__(self, size: Tuple[int, int]):
        pygame.init()
        self.is_new = None
        self.cells = None
        self.size = size
        self.display = pygame.display.set_mode(size)
        self.display.fill(colors['BG'])

    def start(self):
        self.is_new = True
        self.cells = Cells(self.n_cells())
        while self.is_new:
            self.check_event()
            pygame.display.update()
            render(self.display, self.cells.matrix)
        self.play()

    def n_cells(self) -> Tuple[int, int]:
        cols, rows = self.size
        cols /= CELL_WIDTH
        rows /= CELL_WIDTH
        return int(cols),int(rows)

    def play(self):
        self.is_new = False
        for matrix in self.cells:
            self.check_event()
            render(self.display, matrix)
            pygame.display.update()
            sleep(SPEED)


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.is_new:
                x, y = pygame.mouse.get_pos()
                x, y = int(x / CELL_WIDTH), int(y / CELL_WIDTH)
                self.cells.matrix[x][y] = (self.cells.matrix[x][y] + 1) % NB_STATE
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.play()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_r:
                    self.start()
            if event.type == pygame.QUIT:
                pygame.quit()


def render(display: pygame.display, matrix: np.array):
    for x in range(matrix.shape[1]):
        for y in range(matrix.shape[0]):
            cell = Cell(CELL_WIDTH, (x, y), color_ids[matrix[x][y] + 1])
            box(display, (cell.position, cell.shape), cell.color)
