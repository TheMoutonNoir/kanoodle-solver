class DLXNode:
    def __init__(self, row, col):
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.row = row
        self.col = col


class HeaderNode(DLXNode):
    def __init__(self, col):
        super().__init__(None, col)
        self.size = 0  # Number of nodes in this column


def add_node(above, left, row, col):
    new_node = DLXNode(row, col)
    # Link horizontally
    new_node.left = left
    new_node.right = left.right
    left.right.left = new_node
    left.right = new_node
    # Link vertically
    new_node.up = above
    new_node.down = above.down
    above.down.up = new_node
    above.down = new_node
    col.size += 1
    return new_node


def make_dancing_links_matrix(board, pieces):
    num_cells = board.size_x * board.size_y
    num_constraints = num_cells + len(pieces)
    header = HeaderNode("header")
    column_nodes = [HeaderNode(c) for c in range(num_constraints)]

    # Link headers
    prev = header
    for node in column_nodes:
        node.right = prev.right
        node.left = prev
        prev.right.left = node
        prev.right = node
        prev = node

    # Create rows for each piece placement
    for i, piece in enumerate(pieces):
        for placement in board.find_possible_placements(piece):
            leftmost = None
            row_start = None
            for pos in placement.positions:
                col = column_nodes[pos]
                above = col.up
                if not leftmost:
                    leftmost = add_node(above, col, placement, col)
                    row_start = leftmost
                else:
                    add_node(above, leftmost, placement, col)
            # Piece-used constraint
            piece_col = column_nodes[num_cells + i]
            add_node(piece_col.up, row_start, placement, piece_col)

    return header


def cover(col):
    col.left.right = col.right
    col.right.left = col.left
    row = col.down
    while row != col:
        node = row.right
        while node != row:
            node.down.up = node.up
            node.up.down = node.down
            node.col.size -= 1
            node = node.right
        row = row.down


def uncover(col):
    row = col.up
    while row != col:
        node = row.left
        while node != row:
            node.col.size += 1
            node.down.up = node
            node.up.down = node
            node = node.left
        row = row.up
    col.left.right = col
    col.right.left = col


def solve_dlx(header):
    if header.right == header:
        return []  # Solution found

    c = header.right
    while c != header and c.size == 0:
        c = c.right
    if c == header:
        return None  # No solution

    cover(c)
    r = c.down
    while r != c:
        solution = [r.row]
        node = r.right
        while node != r:
            cover(node.col)
            node = node.right

        result = solve_dlx(header)
        if result:
            return solution + result

        node = r.left
        while node != r:
            uncover(node.col)
            node = node.left

        r = r.down
    uncover(c)
    return None


# Example usage
def solve(board, pieces):
    header = make_dancing_links_matrix(board, pieces)
    solution = solve_dlx(header)
    return solution
