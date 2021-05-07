from utils import ALIVE, DEAD, kernel_3x3
import numpy as np
from scipy import signal

class Rules():
    def game_live(matrix: np.array) -> np.array:
        nb_neighbours = signal.convolve2d(matrix, kernel_3x3, mode='same')
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                if matrix[x][y] == DEAD and nb_neighbours[x][y] == 3:
                    matrix[x][y] = ALIVE
                elif matrix[x][y] == ALIVE and nb_neighbours[x][y] == 2 or nb_neighbours[x][y] == 3:
                    matrix[x][y] = ALIVE
                else :
                    matrix[x][y] = DEAD
        return matrix
