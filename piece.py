import numpy as np


class Piece:
    def __init__(self, shape, transposed=False, hflipped=False, vflipped=False):
        self.transposed = transposed
        self.hflipped = hflipped
        self.vflipped = vflipped
        self.shape = shape
        if transposed:
            self.transposePiece()
        if hflipped:
            self.hflipPiece()
        if vflipped:
            self.vflipPiece()

    def transposePiece(self):
        self.shape.value.space = np.transpose(self.shape.value.space)
        self.transposed = not self.transposed

    def hflipPiece(self):
        self.shape.value.space = np.flip(self.shape.value.space)
        self.hflipped = not self.hflipped

    def vflipPiece(self):
        self.shape.value.space = np.flip(self.shape.value.space, axis=1)
        self.vflipped = not self.vflipped

    def printShape(self):
        for row in self.shape.value.space:
            print(row)
