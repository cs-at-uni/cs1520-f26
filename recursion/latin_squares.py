'''
  Latin Squares Solver: given a partially-completed Latin Square, fill in
                        the blanks with legal values
    
    * an N x N square with N symbols where each symbol appears exactly once
      in each row and exactly once in each column

    * We'll solve it using "backtracking"
'''

def solve_square(square, row, col):
    # Base case 1: column is all checked
    if row >= len(square):
        return solve_square(square, 0, col + 1)

    # Base case 2: all columns have been checked
    if col >= len(square):
        return True

    # Base case 3: value already exists in this spot
    if square[row][col] != -1:
        return solve_square(square, row + 1, col)

    # Recursive step:
    # * for every [legal?] symbol:
    #   * [[if symbol is legal for the given position (row, col),
    #     then]]:
    #       * put it in the position and recurse, checking
    #         the next position
    #       * if you solved it, return True
    for possible_symbol in range(len(square)):
        if is_legal(possible_symbol, square, row, col):
            square[row][col] = possible_symbol
            if solve_square(square, row + 1, col):
                return True

    # * if you get this far, it isn't solveable, so return False
    return False


def is_legal(symbol, square, row, col):
    return True