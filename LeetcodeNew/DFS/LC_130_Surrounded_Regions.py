#The key idea is replace O that not connected with edges to X

import collections

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                #If the edge contains O, do DFS -- replace O to V
                if (i == 0 or i == len(board ) -1 or j == 0 or j == len(board[0] ) -1) and board[i][j] == 'O':
                    self.dfs(board, i, j)
        #Final step, replace V to O, non-V to X
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        #replace O to V
        if board[i][j] == 'O':
            board[i][j] = 'V'
            #Recursive the the neighbors if neighbors is also O
            if i > 0 and board[ i -1][j] == 'O':
                self.dfs(board, i- 1, j)
            if j > 1 and board[i][j - 1] == 'O':
                self.dfs(board, i, j - 1)
            if i < len(board) - 1 and board[i + 1][j] == 'O':
                self.dfs(board, i + 1, j)
            if j < len(board[0]) - 1 and board[i][j + 1] == 'O':
                self.dfs(board, i, j + 1)


#Same idea for BFS, add surrounded area into queue and check if edge neighbors area
class Solution2:
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








