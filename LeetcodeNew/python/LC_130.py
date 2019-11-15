
class Solution:
    def solve(self, board):
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            self.dfs(i, 0, board, m, n)
            self.dfs(i, n- 1, board, m, n)

        for j in range(1, n - 1):
            self.dfs(0, j, board, m, n)
            self.dfs(m - 1, j, board, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def dfs(self, i, j, board, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = 'D'
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            self.dfs(x, y, board, m, n)





