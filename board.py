import numpy as np

from const import *
from square import Square
from piece import *

class Board():

    def __init__(self):
        self.squares = np.zeros((N_ROWS, N_COLS))

        self._create()
        self._add_piece("white")
        self._add_piece("black")

    def _create(self):
        for row in range(N_COLS):
            for col in range(N_ROWS):
                self.squares[row][col] = Square(row, col)

    def _add_piece(self, color):
        if color == "white":
            row_pawn, row_other = (6, 7)
        else:
            row_pawn, row_other = (1, 0)

        for col in range(N_COLS):
            self.squares[row_pawn] = Square(row_pawn, col, Pawn(color))
        
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        self.squares[row_other][4] = Square(row_other, 4, King(color))