from board import Board
from piece import Piece
from noodle import Noodle

def main():
    b = Board(5,11)
    p = Piece(3,1,Noodle.A)
    p2 = Piece(2,0, Noodle.I)
    p.transposePiece()
    p.flipPiece()
    p2.transposePiece()
    # p.transposePiece()
    # print(p.beenFlipped)
    # print(p.beenTransposed)
    # p.printShape()
    b.insertPiece(p)
    b.insertPiece(p2)
    # b.printBoard()
    # print(p.shape.value.weight)

if __name__ == "__main__":
    main()
