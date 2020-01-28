"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.







Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.



Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.


Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.

"""

"""
解题方法
如果dfs的话一定会超时的，所以还是得用dp来解。

这个dp数组代表在某一轮中，这个马能到这个位置的次数。

dp更新的策略是，我们遍历棋盘的每个位置，当前的数值是能走到这个位置的在上一轮dp的数值 + 1。

这个题的对称性让这个题变得简单而又有趣。最内层的for循环对dp进行更新的时候是不用考虑索引位置的，因为对称性太美了。

时间复杂度是O(K * N ^ 2)，空间复杂度是O(N ^ 2)。

注意，python2里面的/默认的是地板除，需要用float再除得到概率。
"""


class Solution:
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            temp = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            temp[r+dr][c+dc] += val / 8.0
            dp = temp
        return sum(map(sum, dp))







