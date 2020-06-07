"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""
import collections

class Solution:
    def solve(self, board) -> None:
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            self.dfs(board, i, 0, m, n)
            self.dfs(board, i, n - 1, m, n)

        for j in range(n):
            self.dfs(board, 0, j, m, n)
            self.dfs(board, m - 1, j, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def dfs(self, board, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = '#'
        for direction in self.directions:
            x = i + direction[0]
            y = j + direction[1]
            self.dfs(board, x, y, m, n)



class SolutionBFS:
    def solve(self, board):
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r - 1, c));
                queue.append((r + 1, c))
                queue.append((r, c - 1));
                queue.append((r, c + 1))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"





class SolutionTony:
    def solve(self, board) -> None:
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            if board[i][0] == 'O':
                self.bfs(board, i, 0)
            if board[i][n - 1] == 'O':
                self.bfs(board, i, n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                self.bfs(board, 0, j)
            if board[m - 1][j] == 'O':
                self.bfs(board, m - 1, j)

        print(board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def bfs(self, board, i, j):
        m, n = len(board), len(board[0])
        queue = collections.deque()
        queue.append([i, j])
        board[i][j] = '#'

        while queue:
            node = queue.popleft()
            for dx, dy in self.directions:
                x = node[0] + dx
                y = node[1] + dy
                if x < 0 or y < 0 or x >= m or y >= n:
                    continue

                if board[x][y] != 'O':
                    continue

                board[x][y] = '#'
                queue.append([x, y])




board = [["O","O","O"],["O","O","O"],["O","O","O"]]
a = SolutionTony()
print(a.solve(board))



