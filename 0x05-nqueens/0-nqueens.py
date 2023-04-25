#!/usr/bin/python3
import sys


def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col, solutions):
        if col == n:
            solution = []
            for row in range(n):
                solution.append(''.join(str(board[row][i]) for i in range(n)))
            solutions.append(solution)
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, col + 1, solutions)
                board[row][col] = 0

    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []
    solve(board, 0, solutions)

    for solution in solutions:
        print(','.join(solution))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
