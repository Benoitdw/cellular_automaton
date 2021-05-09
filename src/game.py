import pygame
import numpy as np
from pygame.gfxdraw import box
from welcome_screen import WelcomeScreen
from utils import colors, CELL_WIDTH, color_ids, SPEED, NB_STATE
from cellular_automaton.src.matrix import Cells, Cell
from typing import Tuple
from time import sleep
import os


class Game:
    def __init__(self, size: Tuple[int, int]):
        pygame.init()
        self.is_running = None
        self.is_new = True
        self.cells = None
        self.size = size
        self.display = pygame.display.set_mode(size)
        bg_path = os.path.join('/'.join(__file__.split('/')[:-2]), 'assets/background.jpg')
        bg = pygame.image.load(bg_path)
        self.display.blit(bg, (0,0))
        self.start_game()

    def start_game(self):
        welcome_screen = WelcomeScreen(self)
        while self.is_new:
            welcome_screen.render()

    def init_grid(self):
        self.is_running = True
        self.cells = Cells(self.n_cells())
        while self.is_running:
            self.check_event()
            pygame.display.update()
            render(self.display, self.cells.matrix)
        self.play()

    def n_cells(self) -> Tuple[int, int]:
        cols, rows = self.size
        cols /= CELL_WIDTH
        rows /= CELL_WIDTH
        return int(cols), int(rows)

    def play(self):
        self.is_running = False
        for matrix in self.cells:
            self.check_event()
            render(self.display, matrix)
            pygame.display.update()
            sleep(SPEED)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.is_running:
                x, y = pygame.mouse.get_pos()
                x, y = int(x / CELL_WIDTH), int(y / CELL_WIDTH)
                self.cells.matrix[x][y] = (self.cells.matrix[x][y] + 1) % NB_STATE
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.play()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_r:
                    self.init_grid()
            if event.type == pygame.QUIT:
                pygame.quit()


def render(display: pygame.display, matrix: np.array):
    for x in range(matrix.shape[1]):
        for y in range(matrix.shape[0]):
            cell = Cell(CELL_WIDTH, (x, y), color_ids[matrix[x][y] + 1])
            box(display, (cell.position, cell.shape), cell.color)
