import numpy as np
from noodle import Noodle
from board import Board


class Piece:
    def __init__(
        self, shape, is_transposed=False, is_hflipped=False, is_vflipped=False
    ):
        self.original_shape = shape
        self.is_transposed = is_transposed
        self.is_hflipped = is_hflipped
        self.is_vflipped = is_vflipped
        self.shape = self.apply_transformations(shape)

    def apply_transformations(self, shape):
        if self.is_transposed:
            shape = shape.transpose()
        if self.is_hflipped:
            shape = shape.hflip()
        if self.is_vflipped:
            shape = shape.vflip()
        return shape

    def __str__(self):
        return np.array_str(self.shape.space)

    def get_transposed(self):
        return Piece(
            self.original_shape,
            not self.is_transposed,
            self.is_hflipped,
            self.is_vflipped,
        )

    def get_hflipped(self):
        return Piece(
            self.original_shape,
            self.is_transposed,
            not self.is_hflipped,
            self.is_vflipped,
        )

    def get_vflipped(self):
        return Piece(
            self.original_shape,
            self.is_transposed,
            self.is_hflipped,
            not self.is_vflipped,
        )

    def draw_piece(self):
        b = Board(20, 20)
        b.place_piece(self, 5, 5)
        b.print_board()

    def unique_transformations(self):
        transformations = set()
        unique_pieces = []

        for is_transposed in [True, False]:
            for is_hflipped in [True, False]:
                for is_vflipped in [True, False]:
                    transformed_piece = self.get_transposed() if is_transposed else self
                    transformed_piece = (
                        transformed_piece.get_hflipped()
                        if is_hflipped
                        else transformed_piece
                    )
                    transformed_piece = (
                        transformed_piece.get_vflipped()
                        if is_vflipped
                        else transformed_piece
                    )
                    piece_str = str(transformed_piece)
                    if piece_str not in transformations:
                        transformations.add(piece_str)
                        unique_pieces.append(transformed_piece)
        return unique_pieces
