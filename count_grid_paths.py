'''
Given a MxN grid, find the total number of possible paths from the
top left corner to the bottom right corner if you can only move right
or down from each cell

O(MN)
'''


def count_paths(m, n):
    grid = []
    for i in range(m):
        grid.append([])
        for j in range(n):
            grid[i].append(0)

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                # in first row or first column
                # need to make them 1 to populate predecessor values
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

    print grid

    # bottom right corner will contain the number of times we landed on cell
    return grid[m - 1][n - 1]


print count_paths(5, 5)
