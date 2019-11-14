
class Solution:
    def solveSudoku(self, board):
        self.dfs(board)

    def dfs(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for char in '123456789':
                        board[row][col] = char
                        if self.isValid(board, row, col) and self.dfs(board):
                            return True
                        board[row][col] = '.'
                    return False
        return True


    def isValid(self, board, i, j):
        temp = board[i][j]
        board[i][j] = '.'
        for num in range(9):
            if board[num][j] == temp or board[i][num] == temp:
                return False

        for row in range(3):
            for col in range(3):
                if board[( i//3 ) *3 + row][( j//3 ) *3 + col] == temp:
                    return False
        board[i][j] = temp
        return True

