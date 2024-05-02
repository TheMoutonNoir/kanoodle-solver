import numpy as np
from noodle import Noodle


class Piece:
    def __init__(
        self, shape, is_transposed=False, is_hflipped=False, is_vflipped=False
    ):
        self.shape = shape
        self.is_transposed = is_transposed
        self.is_hflipped = is_hflipped
        self.is_vflipped = is_vflipped
        self._apply_transformations()

    def _apply_transformations(self):
        if self.is_transposed:
            self.shape.value.space = np.transpose(self.shape.value.space)
        if self.is_hflipped:
            self.shape.value.space = np.flip(self.shape.value.space, axis=1)
        if self.is_vflipped:
            self.shape.value.space = np.flip(self.shape.value.space, axis=0)

    def __str__(self):
        return np.array_str(self.shape.value.space)

    def get_transposed(self):
        return Piece(
            self.shape, not self.is_transposed, self.is_hflipped, self.is_vflipped
        )

    def get_hflipped(self):
        return Piece(
            self.shape, self.is_transposed, not self.is_hflipped, self.is_vflipped
        )

    def get_vflipped(self):
        return Piece(
            self.shape, self.is_transposed, self.is_hflipped, not self.is_vflipped
        )

    def unique_transformations(self):
        transformations = set()
        unique_pieces = []

        for is_transposed in [True, False]:
            for is_hflipped in [True, False]:
                for is_vflipped in [True, False]:
                    transformed_piece = Piece(
                        self.shape, is_transposed, is_hflipped, is_vflipped
                    )
                    piece_str = str(transformed_piece)
                    if piece_str not in transformations:
                        transformations.add(piece_str)
                        unique_pieces.append(transformed_piece)
        return unique_pieces
