import numpy as np


class Board:
    def __init__(self, size_x, size_y):
        self.board = np.full((size_y, size_x), ".", dtype=str)
        self.size_x = size_x
        self.size_y = size_y

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def place_piece(self, piece, y, x):
        piece_shape = piece.shape.value.space
        piece_name = piece.shape.value.name

        end_y, end_x = y + piece_shape.shape[0], x + piece_shape.shape[1]
        if end_y > self.size_y or end_x > self.size_x:
            return False

        target_area = self.board[y:end_y, x:end_x]
        if np.any((target_area != ".") & (piece_shape == 1)):
            return False

        self.board[y:end_y, x:end_x][piece_shape == 1] = piece_name
        return True

    def remove_piece(self, piece, y, x):
        piece_shape = piece.shape.value.space
        for dy in range(piece_shape.shape[0]):
            for dx in range(piece_shape.shape[1]):
                if piece_shape[dy, dx] == 1:
                    self.board[y + dy, x + dx] = "."

        return True

    def find_possible_placements(self, piece):
        possible_places = []
        piece_shape = piece.shape.value.space
        for y in range(self.size_y):
            for x in range(self.size_x):
                if (
                    y + piece_shape.shape[0] <= self.size_y
                    and x + piece_shape.shape[1] <= self.size_x
                ):
                    if self.can_place(piece, y, x):
                        possible_places.append((x, y))
        return possible_places

    def can_place(self, piece, y, x):
        piece_shape = piece.shape.value.space
        target_area = self.board[
            y : y + piece_shape.shape[0], x : x + piece_shape.shape[1]
        ]
        return not np.any((target_area != ".") & (piece_shape == 1))
