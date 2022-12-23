
class Piece():
    def __init__(self, name, color, value, texture, texture_rect= None):
        pass


class Pawn(Piece):
    def __init__(self, color):
        self.direction = -1 if color == "white" else 1
        
        super().__init__("pawn", color, 1)


class Knight(Piece):
    def __init__(self, color):
        super().__init__("pawn", color, 3)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__("pawn", color, 3.01)


class Rook(Piece):
    def __init__(self, color):
        super().__init__("pawn", color, 5)


class Queen(Piece):
    def __init__(self, color):
        super().__init__("pawn", color, 9)


class King(Piece):
    def __init__(self, color):
        super().__init__("pawn", color, 10000)





