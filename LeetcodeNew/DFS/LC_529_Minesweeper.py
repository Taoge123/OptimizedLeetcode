"""
This is a typical Search problem, either by using DFS or BFS. Search rules:

1. If click on a mine ('M'), mark it as 'X', stop further search.
2. If click on an empty cell ('E'), depends on how many surrounding mine:
   2.1 Has surrounding mine(s), mark it with number of surrounding mine(s), stop further search.
   2.2 No surrounding mine, mark it as 'B', continue search its 8 neighbors.
"""

#map(function_to_apply, list_of_inputs)

class Solution:
    def updateBoard(self, board, click):
        row, col = click[0], click[1]
        directions =  ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            #If we got mine, then return
            if board[row][col] == 'M':
                board[row][col] = 'X'
            #IF the board is unrevaaled, n is the count of mine around current spot
            elif board[row][col] == 'E':
                count = sum([board[row + r][col + c] == 'M' for r, c in directions if 0 <= row + r < len(board) and 0 <= col + c < len(board[0])])
                board[row][col] = count and str(count) or 'B'
                print((board,) * 8)
                not count and map(self.updateBoard, (board,) * 8, [(row + d[0], col + d[1]) for d in directions])
        return board

#Understanding solution
class SolutionWithoutMap:
    def updateBoard(self, board, click):
        row, col = click[0], click[1]
        directions =  ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            #If we got mine, then return
            if board[row][col] == 'M':
                board[row][col] = 'X'
            #IF the board is unrevaaled, n is the count of mine around current spot
            elif board[row][col] == 'E':
                count = sum([board[row + r][col + c] == 'M' for r, c in directions if 0 <= row + r < len(board) and 0 <= col + c < len(board[0])])
                board[row][col] = count and str(count) or 'B'
                # print((board,) * 8)
                if not count:
                    for d in directions:
                        self.updateBoard(board, (row + d[0], col + d[1]))
        return board


class Solution2:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return []

        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        # If a mine ('M') is revealed, then the game is over - change it to 'X'.
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        # run dfs to reveal the board
        self.dfs(board, i, j)
        return board

    def dfs(self, board, i, j):
        if board[i][j] != 'E':
            return

        m, n = len(board), len(board[0])
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

        mine_count = 0

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                mine_count += 1

        if mine_count == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(mine_count)
            return

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs(board, ni, nj)


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        r, c = click[0], click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        m, n = len(board), len(board[0])

        def numMines(row, col):
            return sum(row + x[0] >= 0 and row + x[0] < m and col + x[1] >= 0 and col + x[1] < n and board[row + x[0]][
                col + x[1]] == 'M' for x in [(-1, 0), (1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1), (0, 1), (0, -1)])

        def recurse(row, col):
            if board[row][col] != 'E': return
            nMine = numMines(row, col)
            if nMine == 0:
                board[row][col] = 'B'
                for x in [(-1, 0), (1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1), (0, 1), (0, -1)]:
                    if row + x[0] >= 0 and row + x[0] < m and col + x[1] >= 0 and col + x[1] < n: recurse(row + x[0],
                                                                                                          col + x[1])
            else:
                board[row][col] = str(nMine)

        recurse(r, c)
        return board

a = SolutionWithoutMap()
input = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

click = [3,0]

print(a.updateBoard(input, click))



