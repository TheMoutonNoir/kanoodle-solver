from board import Board
from piece import Piece
from noodle import Noodle
from solve import solve


def main():
    b = Board(11, 5)
    p1 = Piece(Noodle.K.value)
    p2 = Piece(Noodle.E.value, is_transposed=True, is_vflipped=True)
    b.place_piece(p1, 1, 1)
    b.place_piece(p2, 3, 3)

    p3 = Piece(Noodle.A.value)
    p4 = Piece(Noodle.B.value)
    p5 = Piece(Noodle.C.value)
    p6 = Piece(Noodle.D.value)
    p7 = Piece(Noodle.F.value)
    p8 = Piece(Noodle.G.value)
    p9 = Piece(Noodle.H.value)
    p10 = Piece(Noodle.I.value)
    p11 = Piece(Noodle.J.value)
    p12 = Piece(Noodle.L.value)

    pieces = [p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]

    solution = solve(b, pieces)

    if solution:
        solution.print_board()
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
