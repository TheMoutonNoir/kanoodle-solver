from board import Board
from piece import Piece
from noodle import Noodle
from solve import solve


def main():
    b = Board(11, 5)
    p1 = Piece(Noodle.K)
    p2 = Piece(Noodle.E, is_transposed=True, is_vflipped=True)
    b.place_piece(p1, 1, 1)
    b.place_piece(p2, 3, 3)

    p3 = Piece(Noodle.A)
    p4 = Piece(Noodle.B)
    p5 = Piece(Noodle.C)
    p6 = Piece(Noodle.D)
    p7 = Piece(Noodle.F)
    p8 = Piece(Noodle.G)
    p9 = Piece(Noodle.H)
    p10 = Piece(Noodle.I)
    p11 = Piece(Noodle.J)
    p12 = Piece(Noodle.L)

    pieces = [p3, p4, p5, p6, p7, p8]

    solution = solve(b, pieces)

    if solution:
        solution.print_board()
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
