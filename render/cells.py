from typing import Tuple
from dataclasses import dataclass
import numpy as np
from cellular_automaton.constantes import colors, CELL_WIDTH
from pygame.gfxdraw import box


class Cell:
    def __init__(self, width: int, position: Tuple[int, int], color: str):
        self.shape = self.set_shape(width)
        self.position = self.set_position(position)
        self.color = colors[color]

    @staticmethod
    def set_shape(width: int) -> Tuple[int, int]:
        return width, width

    def set_position(self, position: Tuple[int, int]) -> Tuple[int, int]:
        return tuple(x*y for x, y in zip(self.shape, position))


class Cells:
    def __init__(self, shape: Tuple[int, int]):
        self.matrix = np.empty(shape, dtype=Cell)
        self.shape = shape
        self.damier_pattern()

    def damier_pattern(self):
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if y % 2 == 0:
                    if x % 2 == 0:
                        self.matrix[x, y] = Cell(CELL_WIDTH, (x,y), 'BLUE')
                    else:
                        self.matrix[x, y] = Cell(CELL_WIDTH, (x, y), 'VIOLET')
                else:
                    if x % 2 == 0:
                        self.matrix[x, y] = Cell(CELL_WIDTH, (x,y), 'VIOLET')
                    else:
                        self.matrix[x, y] = Cell(CELL_WIDTH, (x, y), 'BLUE')

    def show(self, display):
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                cell = self.matrix[x, y]
                print(cell)
                box(display, (cell.position, cell.shape), cell.color)


class CellsHexa(Cells):
    def __init__(self):
        pass
