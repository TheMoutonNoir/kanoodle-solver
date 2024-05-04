import numpy as np


class Board:
    def __init__(self, size_x, size_y):
        self.board = np.full((size_y, size_x), ".", dtype=str)
        self.size_x = size_x
        self.size_y = size_y
        self.pieces = []
        self.piece_weights = 0

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def place_piece(self, piece, x, y):
        piece_shape = piece.shape.space
        piece_name = piece.shape.name

        end_y, end_x = y + piece_shape.shape[0], x + piece_shape.shape[1]
        if end_y > self.size_y or end_x > self.size_x:
            return False

        target_area = self.board[y:end_y, x:end_x]
        if np.any((target_area != ".") & (piece_shape == 1)):
            return False

        self.board[y:end_y, x:end_x][piece_shape == 1] = piece_name
        self.pieces.append((piece, x, y))
        self.piece_weights += piece.shape.weight
        return True

    def remove_piece(self, piece, x, y):
        piece_shape = piece.shape.space
        for dy in range(piece_shape.shape[0]):
            for dx in range(piece_shape.shape[1]):
                if piece_shape[dy, dx] == 1:
                    self.board[y + dy, x + dx] = "."

        return True

    def find_possible_placements(self, piece):
        possible_places = []
        piece_shape = piece.shape.space
        for y in range(self.size_y):
            for x in range(self.size_x):
                if (
                    y + piece_shape.shape[0] <= self.size_y
                    and x + piece_shape.shape[1] <= self.size_x
                ):
                    if self.can_place(piece, x, y):
                        possible_places.append((x, y))
        return possible_places

    def can_place(self, piece, x, y):
        piece_shape = piece.shape.space
        target_area = self.board[
            y : y + piece_shape.shape[0], x : x + piece_shape.shape[1]
        ]
        return not np.any((target_area != ".") & (piece_shape == 1))

    def copy_board(self):
        # Create a new instance of Board with the same dimensions
        new_board = Board(self.size_x, self.size_y)
        # Copy the array data
        new_board.board = self.board.copy()
        # Copy the list of placed pieces
        new_board.pieces = self.pieces.copy()
        # Copy the total weight of placed pieces
        new_board.piece_weights = self.piece_weights
        return new_board
