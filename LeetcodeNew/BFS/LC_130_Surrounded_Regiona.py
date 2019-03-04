
"""
Given a 2D board containing 'X' and 'O' (the letter O),
capture all regions surrounded by 'X'.

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

Surrounded regions shouldn’t be on the border,
which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O'
on the border will be flipped to 'X'. Two cells are connected
if they are adjacent cells connected horizontally or vertically.
"""
import collections


class SolutionBFS:
    # BFS
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
                queue.append((r - 1, c))
                queue.append((r + 1, c))
                queue.append((r, c - 1))
                queue.append((r, c + 1))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"





class SolutionDFS:
    def solve(self, board):
        if len(board) == 0:
            return
        height = len(board)
        width = len(board[0])
        def dfs(board, y, x):
            if x < 0 or x >= width or y < 0 or y >= height or board[y][x] != 'O':
                return
            board[y][x] = 'S'
            dfs(board, y + 1, x)
            dfs(board, y - 1, x)
            dfs(board, y, x + 1)
            dfs(board, y, x - 1)
        for i in range(width):
            if board[0][i] == 'O':
                dfs(board, 0, i)
            if board[height-1][i] == 'O':
                dfs(board, height-1, i)
        for j in range(height):
            if board[j][0] == 'O':
                dfs(board, j, 0)
            if board[j][width-1] == 'O':
                dfs(board, j, width-1)
        for y in range(height):
            for x in range(width):
                if board[y][x] == 'S':
                    board[y][x] = 'O'
                else:
                    board[y][x] = 'X'





