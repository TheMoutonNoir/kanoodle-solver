def solve(board, pieces):
    if not pieces:
        return board
    else:
        piece = pieces[0]
        for x in range(board.size_x):
            for y in range(board.size_y):
                if (
                    board.placePiece(piece, x, y)
                    or board.placePiece(piece.transposed(), x, y)
                    or board.placePiece(piece.hflipped(), x, y)
                    or board.placePiece(piece.vflipped(), x, y)
                    or board.placePiece(piece.transposed().hflipped(), x, y)
                    or board.placePiece(piece.transposed().vflipped(), x, y)
                    or board.placePiece(piece.hflipped().vflipped(), x, y)
                    or board.placePiece(piece.transposed().hflipped().vflipped(), x, y)
                ):
                    board.printBoard()
                    remaining_pieces = pieces[1:]
                    solution = solve(board, remaining_pieces)
                    if solution:
                        return solution
                    else:
                        board.removePiece(piece, x, y)
                else:
                    continue
