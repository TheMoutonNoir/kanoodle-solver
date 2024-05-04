from board import Board
from piece import Piece
from noodle import Noodle
from solve import solve


def demo():
    b = Board(11, 5)
    p1 = Piece(Noodle.K.value)
    p2 = Piece(Noodle.E.value, is_transposed=True, is_hflipped=True)
    b.place_piece(p1, 2, 1)
    b.place_piece(p2, 4, 3)

    print("Initial board:")
    b.print_board()

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

    if not solution:
        print("No solution found")
    else:
        for s in solution:
            s.print_board()
        print(f"Found {len(solution)} solutions.")


def main():
    b = Board(11, 5)
    p1 = Piece(Noodle.K.value)
    p2 = Piece(Noodle.E.value)
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

    pieces = [p1, p2, p3, p4, p5, p6, p8, p9, p10, p11, p12]

    b.place_piece(p7, 0, 0)

    print("Initial board:")
    b.print_board()

    solution = solve(b, pieces)

    if not solution:
        print("No solution found")
    else:
        for s in solution:
            s.print_board()
        print(f"Found {len(solution)} solutions.")


if __name__ == "__main__":
    main()
