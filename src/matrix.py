from typing import Tuple
import numpy as np
from utils import colors, CELL_WIDTH, color_ids

from rules import Rules


class Cell:
    def __init__(self, width: int, position: Tuple[int, int], color=str):
        self._shape = self.set_shape(width)
        self.position = self.set_position(position)
        self.color = colors[color]

    @staticmethod
    def set_shape(width: int) -> Tuple[int, int]:
        return width, width

    def get_shape(self) -> Tuple[int, int]:
        return tuple(width -1 for width in self._shape)

    shape = property(get_shape, set_shape)

    def set_position(self, position: Tuple[int, int]) -> Tuple[int, int]:
        return tuple(x * y for x, y in zip(self._shape, position))


class Cells:
    def __init__(self, shape: Tuple[int, int]) -> None:
        self.matrix = np.zeros(shape, dtype=int)
        self.shape = shape

    def apply_rule(self) -> np.array:
        self.matrix = Rules.game_live(self.matrix)

    def color_choice(self, value: int) -> str:
        return color_ids[str(value)]

    def __iter__(self):
        while True:
            yield self.matrix
            array_old = self.matrix.copy()
            self.apply_rule()

