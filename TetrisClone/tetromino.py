from enum import Enum
import random
from TetrisClone import GameBoard

class Shape(Enum):
    I_SHAPE = 1
    J_SHAPE = 2
    L_SHAPE = 3
    O_SHAPE = 4
    S_SHAPE = 5
    T_SHAPE = 6
    Z_SHAPE = 7

class Tetromino:
    from TetrisClone import GameBoard
    def __init__(self, shape):
        self.shape = shape
        self.rotation = 0
        self.x = 5
        self.y = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

    def get_rotation_shape(self):
        if self.shape == Shape.I_SHAPE:
            if self.rotation == 0 or self.rotation == 2:
                return [0, 1, 2, 3]
            else:
                return [0, 10, 20, 30]
        elif self.shape == Shape.J_SHAPE:
            if self.rotation == 0:
                return [0, 1, 2, 12]
            elif self.rotation == 1:
                return [0, 1, 11, 21]
            elif self.rotation == 2:
                return [2, 12, 13, 14]
            else:
                return [0, 10, 20, 21]
        elif self.shape == Shape.L_SHAPE:
            if self.rotation == 0:
                return [2, 0, 1, 12]
            elif self.rotation == 1:
                return [0, 10, 20, 21]
            elif self.rotation == 2:
                return [0, 1, 2, 14]
            else:
                return [0, 1, 11, 21]
        elif self.shape == Shape.O_SHAPE:
            return [0, 1, 10, 11]
        elif self.shape == Shape.S_SHAPE:
            if self.rotation == 0 or self.rotation == 2:
                return [1, 2, 12, 13]
            else:
                return [0, 10, 11, 21]
        elif self.shape == Shape.T_SHAPE:
            if self.rotation == 0:
                return [1, 0, 2, 12]
            elif self.rotation == 1:
                return [1, 0, 10, 11]
            elif self.rotation == 2:
                return [1, 0, 2, 11]
            else:
                return [0, 10, 11, 21]
        elif self.shape == Shape.Z_SHAPE:
            if self.rotation == 0 or self.rotation == 2:
                return [0, 1, 11, 12]
            else:
                return [1, 10, 11, 20]

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def can_move_down(self, game_board):
        shape = self.get_rotation_shape()
        for i in range(4):
            for j in range(4):
                if i * 4 + j in shape:
                    if self.y + i + 1 >= game_board.height or game_board.get_block(self.x + j, self.y + i + 1) != 0:
                        return False
        return True
    
    def can_move_left(self, game_board):
        shape = self.get_rotation_shape()
        for i in range(4):
            for j in range(4):
                if i * 4 + j in shape:
                    if self.x + j - 1 < 0 or game_board.get_block(self.x + j - 1, self.y + i) != 0:
                        return False
        return True

    def can_move_right(self, game_board):
        shape = self.get_rotation_shape()
        for i in range(4):
            for j in range(4):
                if i * 4 + j in shape:
                    if self.x + j + 1 >= game_board.width or game_board.get_block(self.x + j + 1, self.y + i) != 0:
                        return False
        return True

    def update_board(self, game_board):
        shape = self.get_rotation_shape()
        for i in range(4):
            for j in range(4):
                if i * 4 + j in shape:
                    game_board.set_block(self.x + j, self.y + i, self.shape.value)

    @staticmethod
    def random_tetromino():
        return Tetromino(random.choice(list(Shape)))
