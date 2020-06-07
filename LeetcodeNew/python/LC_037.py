"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    for char in '123456789':
                        board[i][j] = char
                        if self.isValid(board, i, j) and self.solveSudoku(board):
                            return True
                        board[i][j] = '.'
                    return False

        return True

    def isValid(self, board, row, col):
        temp = board[row][col]
        board[row][col] = '.'
        for num in range(9):
            if board[num][col] == temp or board[row][num] == temp:
                return False

        for i in range(3):
            for j in range(3):
                if board[(row // 3) * 3 + i][(col // 3) * 3 + j] == temp:
                    return False
        board[row][col] = temp
        return True





