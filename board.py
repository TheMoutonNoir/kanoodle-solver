from piece import Piece
from noodle import Noodle
import numpy as np


class Board:
    def __init__(self, size_x, size_y):
        self.fixed_size_2d_list = [[0] * size_x for _ in range(size_y)]
        self.size_x = size_x
        self.size_y = size_y

    # Print the 2D list
    def printBoard(self):
        for x in self.fixed_size_2d_list:
            print(x)
        print()

    def placePiece(self, piece, y, x):
        try:
            tempBoard = np.copy(self.fixed_size_2d_list)
            count_x = 0
            for i in piece.shape.value.space:
                count_y = 0
                for j in i:
                    # Check if the position is within the bounds of the board and if the cell is already occupied
                    if j == 1:
                        if (
                            x + count_x >= tempBoard.shape[0]
                            or y + count_y >= tempBoard.shape[1]
                            or tempBoard[x + count_x, y + count_y] == 1
                        ):
                            print("Position already occupied or out of bounds!")
                            return False
                        tempBoard[x + count_x, y + count_y] = 1
                    count_y += 1
                count_x += 1
            self.fixed_size_2d_list = tempBoard
        except Exception as e:
            print("Could not place the piece on the board!", e)
            return False
        return True

    def removePiece(self, piece, y, x):
        try:
            tempBoard = np.copy(self.fixed_size_2d_list)
            count_x = 0
            for i in piece.shape.value.space:
                count_y = 0
                for j in i:
                    if j == 1:
                        tempBoard[x + count_x, y + count_y] = 0
                    count_y = count_y + 1
                count_x = count_x + 1
            self.fixed_size_2d_list = tempBoard
        except Exception as e:
            print("Could not remove the piece from the board!", e)
            return False
        return True
