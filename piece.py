import numpy as np


class Piece:
    def __init__(self,position_x,position_y,shape):
        self.position_x = position_x
        self.position_y = position_y
        self.beenTransposed = False
        self.beenFlipped = False
        self.shape = shape
    
    def transposePiece(self):
        self.shape.value.space = np.transpose(self.shape.value.space)
        self.beenTransposed = not self.beenTransposed

    def flipPiece(self):
        self.shape.value.space = np.flip(self.shape.value.space)
        self.beenFlipped = not self.beenFlipped


    def printShape(self):
        for row in self.shape.value.space:
            print(row)
    