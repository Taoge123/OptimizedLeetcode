




class Solution:
    def numRookCaptures(self, board) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x0, y0 = i, j

        res = 0
        for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x = x0 + i
            y = y0 + j
            while x >= 0 and x < 8 and y >= 0 and y < 8:
                if board[x][y] == 'p':
                    res += 1

                if board[x][y] != '.':
                    break

                x = x + i
                y = y + j
        return res



