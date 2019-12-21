"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

"""
题目大意
玩一个生存游戏。这个游戏给了一个二维数组，每个数组上写的是这个地方是否有部落。看每个位置的8-连通位置的部落数：

如果一个活着的部落，其周围少于2个部落，这个部落会死
如果一个活着的部落，其周围部落数在2或者3，这个部落活到下一个迭代中
如果一个活着的部落，其周围多于3个部落，这个部落会死
如果一个死了的部落，其周围多于3个部落，这个部落会活
一次迭代是同时进行的，求一轮之后，整个数组。

解题方法
方法很简单暴力，直接求每个位置的8-连通分量并统计部落数就好了，我的做法是先复制了一份，这样使用原始的board去判断部落数，更新放在了新的board_next上不会影响之前的board。最后再把数值复制过来。

时间复杂度是O(MN)，空间复杂度是O(MN).
"""


class Solution:
    def gameOfLife(self, board):
        if not board or len(board[0]) == 0:
            return

        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                count = 0
                for x in range(max(0, i- 1), min(i + 2, m)):
                    for y in range(max(0, j - 1), min(j + 2, n)):
                        if (x, y) != (i, j) and 1 <= board[x][y] <= 2:
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1








