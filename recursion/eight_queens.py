import numpy as np
import copy

N = 8
board = np.zeros([N, N], dtype = int)
board = board.tolist()


# Is it possible to place queen in x,y?
def possible(grid, y, x):

    length_board = len(grid)

    # Check for queens on row y
    for i in range(length_board):
        if board[y][i] == 1:
            return False
    # check for queens on columns x
    for k in range(length_board):
        if board[k][x] == 1:
            return False

    # check diagonals
    for m in range(length_board):
        for n in range(length_board):
            if grid[m][n] == 1:
                if abs(m - y) == abs(n - x):
                    return False

    return True


def solve(board):

    length_of_board = len(board)

    for y in range(length_of_board):
        for x in range(length_of_board):
            if board[y][x] == 0:
                if possible(board, y, x):
                    board[y][x] = 1
                    solve(board)
                    # if we end up here, means we searched through all children branches
                    if sum(sum(a) for a in board) == length_of_board:  # if there are 8 queens
                        return board  # we are successful so return
                    board[y][x] = 0  # remove the previous placed queen
    return board  # means we searched the space, we can return our result

Solution = solve(copy.deepcopy(board)) #get the solution
print(np.asmatrix(Solution))

