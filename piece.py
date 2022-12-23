import os

class Piece():
    def __init__(self, name, color, value, texture= None, texture_rect= None):
        self.name = name
        self.color = color
        self.moves = []
        self.moved = False
        value_sign = 1 if color == "white" else -1
        self.value = value * value_sign

        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size= 80):
        self.texture = os.path.join(
            f"os.path.abspath('.'), 'assets/images/imgs-{size}px/{self.color}_{self.name}.png')")

    def add_moves(self, move):
        self.moves.append(move)

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





