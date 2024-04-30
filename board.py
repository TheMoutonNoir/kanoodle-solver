from piece import Piece
from noodle import Noodle
import numpy as np

class Board:
    def __init__(self,size_x,size_y):
        self.listOfpieces = {
            "A": "","B": "","C": "","D": "","E": "","F": "","G": "","H": "","I": "","K": ""
            }

        # Create a 2D list filled with zeros
        self.fixed_size_2d_list = [[0] * size_y for _ in range(size_x)]
 
    # Print the 2D list
    def printBoard(self):
        for x in self.fixed_size_2d_list:
            print(x)
    
    def insertPiece(self, piece):
        try:
            tempBoard = np.copy(self.fixed_size_2d_list)
            count_x = 0
            for x in piece.shape.value.space:
                count_y = 0
                for y in x:
                    if(y == 1):
                        if(tempBoard[piece.position_x + count_x, piece.position_y + count_y] == 0):
                            tempBoard[piece.position_x + count_x, piece.position_y + count_y] = y 
                            print("reached!")
                        else:
                            return
                    count_y = count_y + 1
                count_x = count_x + 1
            self.fixed_size_2d_list = tempBoard
            for x in tempBoard:
                print(x)
        except Exception as e:
            print("Could not place the piece in the board!", e)
    