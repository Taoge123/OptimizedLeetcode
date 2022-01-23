
"""


Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:



Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem.
For example, you don't need to reveal all the unrevealed mines when the game is over,
consider any cases that you will win the game or flag any squares.
"""

import collections

class Solution:
    def updateBoard(self, board, click):
        if not board:
            return []
        m, n = len(board), len(board[0])
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        self.dfs(board, i, j, m, n)
        return board

    def dfs(self, board, i, j, m, n):
        if board[i][j] != 'E':
             return
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        count = 0
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'M':
                count += 1

        if count == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(count)
            return

        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n:
                self.dfs(board, x, y, m, n)



class SolutionRika:
    def updateBoard(self, board, click):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        m, n = len(board), len(board[0])
        visited = set()
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        elif board[i][j] == 'E':
            self.dfs(directions, board, m, n, i, j, visited)
            return board

    def dfs(self, directions, board, m, n, i, j, visited):
        visited.add((i, j))

        M_cnt = 0
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'M':
                M_cnt += 1
        if M_cnt == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(M_cnt)
            return

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] == 'E':
                self.dfs(directions, board, m, n, x, y, visited)



class Solution2:
    def __init__(self):
        self.directions = [[1 ,0], [0 ,1], [-1 ,0] ,[0 ,-1] ,[1 ,1] ,[-1 ,-1] ,[1 ,-1] ,[-1 ,1]]

    def numBomb(self, board, i, j, m, n):
        count = 0
        for dire in self.directions:
            x = i + dire[0]
            y = j + dire[1]
            if 0 <= x < m and 0 <= y < n and board[x][y] == "M":
                count += 1
        return count

    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        i, j = click[0], click[1]
        if board[i][j] == "M":
            board[i][j] = "X"

        queue = collections.deque()
        queue.append(click)
        visited = set(click)

        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                if board[x][y] == "E":
                    numBomb = self.numBomb(board, x, y, m, n)
                    board[x][y] = 'B' if numBomb == 0 else str(numBomb)
                    if numBomb == 0:
                        for dire in self.directions:
                            newX = x + dire[0]
                            newY = y + dire[1]
                            if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited:
                                queue.append((newX, newY))
                                visited.add((newX, newY))
        return board




board = [['B', '1', 'E', '1', 'B'],
         ['B', '1', 'M', '1', 'B'],
         ['B', '1', '1', '1', 'B'],
         ['B', 'B', 'B', 'B', 'B']]
click = [0,2]

a = Solution2()
print(a.updateBoard(board, click))


