
"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy,
different positive integers board[i][j] represent different types of candies.
A value of board[i][j] = 0 represents that the cell at position (i, j) is empty.
The given board represents the state of the game following the player's move.
Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally,
"crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself,
then these candies will drop until they hit a candy or bottom at the same time.
(No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.

Example:

Input:
board =
[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

Output:
[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

"""

"""
Rotate the board will make the drop operation much easier.
That being said, instead of move all non-zero value to the end of each column, 
the drop operation becomes move all non-zero value to the beginning of each row.
"""


class Solution(object):
    def candyCrush(self, board):
        board = map(list, zip(*reversed(board)))  # rotate clockwise 90 degree
        m, n = len(board), len(board[0])

        # repeat crush and drop
        while True:
            candy = set([])
            # check every row
            for i in range(m):
                for j in range(2, n):
                    if board[i][j] and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        candy |= {(i, j), (i, j - 1), (i, j - 2)}
            # check every col
            for j in range(n):
                for i in range(2, m):
                    if board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        candy |= {(i, j), (i - 1, j), (i - 2, j)}
            if not candy: break
            for i, j in candy: board[i][j] = 0

            # drop the board, move non-zero to the beginning of each row.
            for i in range(m):
                row = filter(None, board[i])
                board[i] = row + [0] * (n - len(row))

        board = list(reversed(map(list, zip(*board))))  # rotate counter-clockwise 90 degree
        return board



class Solution2:
    def candyCrush(self, M):
        while True:
            # 1, Check
            crush = set()
            for i in range(len(M)):
                for j in range(len(M[0])):
                    if j > 1 and M[i][j] and M[i][j] == M[i][j - 1] == M[i][j - 2]:
                        crush |= {(i, j), (i, j - 1), (i, j - 2)}
                    if i > 1 and M[i][j] and M[i][j] == M[i - 1][j] == M[i - 2][j]:
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}

            # 2, Crush
            if not crush: break
            for i, j in crush: M[i][j] = 0

            # 3, Drop
            for j in range(len(M[0])):
                idx = len(M) - 1
                for i in reversed(range(len(M))):
                    if M[i][j]: M[idx][j] = M[i][j]; idx -= 1
                for i in range(idx + 1): M[i][j] = 0
        return M



