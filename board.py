import numpy as np

from const import *
from square import Square

class Board():

    def __init__(self):
        self.squares = np.zeros((N_ROWS, N_COLS))

        self._create()

    def _create(self):
        for row in range(N_COLS):
            for col in range(N_ROWS):
                self.squares[row][col] = Square(row, col)

    def _add_piece(self, color):
        pass

