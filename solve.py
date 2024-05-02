def solve_memo(board, pieces, memo):
    board_key = hash(board.board.tostring())  # Hash the board state for memoization
    pieces_key = tuple(sorted((p.shape.name, p.shape.weight) for p in pieces))
    memo_key = (board_key, pieces_key)

    if memo_key in memo:
        return memo[memo_key]

    if not pieces:
        return board

    # Implement Most Constrained First and Least Constraining Variable
    pieces.sort(key=lambda p: (len(board.find_possible_placements(p)), -p.shape.weight))

    for i, piece in enumerate(pieces):
        possible_places = board.find_possible_placements(piece)
        transformations = piece.unique_transformations()
        for x, y in possible_places:
            for transformed_piece in transformations:
                if board.place_piece(transformed_piece, y, x):
                    remaining_pieces = pieces[:i] + pieces[i + 1 :]
                    solution = solve_memo(board, remaining_pieces, memo)
                    if solution:
                        memo[memo_key] = solution
                        return solution
                    board.remove_piece(transformed_piece, y, x)

    memo[memo_key] = None
    return None


def solve(board, pieces):
    return solve_memo(board, pieces, {})
