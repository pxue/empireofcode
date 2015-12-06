def check_grid(grid):
    for i, row in enumerate(grid):
        # check row alternates
        p = row[0]
        for x in row[1:]:
            if x == p:
                return False
            p = x

    # check column alternates
    for i, v in enumerate(grid[0]):
        p = v
        for j in range(1, len(grid)):
            q = grid[j][i]
            if q == p:
                return False
            p = q

    return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
    #assert check_grid([["X", "Z", "X"],
                       #["Z", "X", "Z"],
                       #["X", "Z", "X"]]), "3x3 Good"
    assert check_grid([["X", "Z", "X", "Z"],
                       ["Z", "X", "Z", "X"]]), "2x4 Good"
    assert not check_grid([["X", "X"],
                           ["X", "X"]]), "2x2 Bad"
    assert not check_grid([["X", "Z", "X"],
                           ["Z", "Z", "Z"],
                           ["X", "Z", "X"]]), "3x3 Bad"
    assert not check_grid([["X", "Z", "X", "Z"],
                           ["X", "Z", "X", "Z"]]), "2x4 Bad"

    print("Use 'Check' to earn sweet rewards!")
