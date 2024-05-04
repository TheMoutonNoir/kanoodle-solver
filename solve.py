from algorithm_x import AlgorithmX


def create_algorithm_x_matrix(board, pieces):
    board_size = board.size_x * board.size_y
    num_columns = board_size + len(pieces)
    solver = AlgorithmX(num_columns)
    piece_id = 0

    print("Creating constraint matrix...")
    for piece in pieces:
        placements = board.find_possible_placements(piece)
        print(
            f"Found {len(placements)} possible placements for piece {piece.shape.name}"
        )
        print(placements)
        print(piece.shape.space)
        for x, y in placements:
            columns = [
                y * board.size_x + x + dy * board.size_x + dx
                for dy in range(piece.shape.space.shape[0])
                for dx in range(piece.shape.space.shape[1])
                if piece.shape.space[dy, dx] == 1
            ]
            columns.append(board_size + piece_id)
            print(f"Appending row for piece {piece.shape.name} at ({x},{y}): {columns}")
            solver.appendRow(columns, (piece.shape.name, piece, x, y))
        piece_id += 1

    return solver


def apply_solution(board, solution):
    print("Applying solution...")
    for s in solution:
        piece_name, transformation, x, y = s
        print(f"Placing piece {piece_name} at ({x},{y})")
        board.place_piece(transformation, y, x)


def solve(board, pieces):
    solver = create_algorithm_x_matrix(board, pieces)
    for solution in solver.solve():
        print("Solution found!")
        print(solution)


# Assume the board and pieces are already defined elsewhere
# board = Board(size_x, size_y)
# pieces = [Piece(shape1), Piece(shape2), ...]
# solution_board = solve(board, pieces)
# if solution_board:
#     solution_board.print_board()
# else:
#     print("No solution found.")
