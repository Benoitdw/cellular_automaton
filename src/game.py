import pygame
import numpy as np
from pygame.gfxdraw import box, vline, hline
from utils import colors, CELL_WIDTH, color_ids, SPEED, NB_STATE
from cellular_automaton.src.matrix import Cells, Cell
from typing import Tuple
from time import sleep


class Game:
    def __init__(self, size: Tuple[int, int]):
        self.is_new = True
        pygame.init()
        self.size = size
        self.display = pygame.display.set_mode(size)
        self.display.fill(colors['BG'])
        self.cells = Cells(self.n_cells())

    def start(self):
        while self.is_new:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    x,y = int(x/CELL_WIDTH), int(y/CELL_WIDTH)
                    self.cells.matrix[x][y] = (self.cells.matrix[x][y] + 1) % NB_STATE
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.play()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
            render(self.display, self.cells.matrix)

    def n_cells(self) -> Tuple[int, int]:
        cols, rows = self.size
        cols /= CELL_WIDTH
        rows /= CELL_WIDTH
        return int(cols),int(rows)

    def play(self):
        self.is_new = False
        for matrix in self.cells:
            self.check_exit()
            render(self.display, matrix)
            pygame.display.update()
            sleep(SPEED)


    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()


def render(display: pygame.display, matrix: np.array):
    for x in range(matrix.shape[1]):
        for y in range(matrix.shape[0]):
            cell = Cell(CELL_WIDTH, (x, y), color_ids[matrix[x][y] + 1])
            box(display, (cell.position, cell.shape), cell.color)
