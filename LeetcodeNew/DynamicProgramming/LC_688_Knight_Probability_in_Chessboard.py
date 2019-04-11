
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
Approach #1: Dynamic Programming [Accepted]
Intuition and Algorithm

Let f[r][c][steps] be the probability of being on square (r, c) after steps steps. 
Based on how a knight moves, we have the following recursion:

f[r][c][steps] = \sum_{dr, dc} f[r+dr][c+dc][steps-1] / 8.0f[r][c][steps]=∑ 
dr,dc
​	
 f[r+dr][c+dc][steps−1]/8.0

where the sum is taken over the eight (dr, dc)(dr,dc) pairs 
(2, 1),(2,1), (2, -1),(2,−1), (-2, 1),(−2,1), (-2, -1),(−2,−1), (1, 2),(1,2), (1, -2),(1,−2), (-1, 2),(−1,2), (-1, -2)(−1,−2).

Instead of using a three-dimensional array f, we will use two two-dimensional ones dp and dp2, 
storing the result of the two most recent layers we are working on. dp2 will represent f[][][steps], and dp will represent f[][][steps-1].

"""
import collections

class Solution1:
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))



class Solution2:
    def knightProbability(self, N, K, r, c):
        memo = {}

        def dfs(i, j, p, k):
            if 0 <= i < N and 0 <= j < N and k < K:
                sm = 0
                for x, y in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
                    if (i + x, j + y, k) not in memo:
                        memo[(i + x, j + y, k)] = dfs(i + x, j + y, p / 8, k + 1)
                    sm += memo[(i + x, j + y, k)]
                return sm
            else:
                return 0 <= i < N and 0 <= j < N and p or 0

        return dfs(r, c, 1, 0)


class Solution3:
    def knightProbability(self, N, K, r, c):

        # O(K*n^2) worst case, keep adding the probability of getting out of the board.
        moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        memo, out_board_p = {(r, c): 1}, 0
        # for each step we will create a new dict to record the onboard coordinates and their probabilities.
        for step in range(K):
            next_memo = collections.defaultdict(int)
            for (i, j), prob in memo.items():
                for d in moves:
                    di, dj = i+d[0], j+d[1]
                    # if the next step is on the board, we record it for next step's calculation
                    if 0<=di<N and 0<=dj<N:
                        next_memo[(di,dj)] += prob * 0.125
                    # if the next step is not on the board, we sum it to our accumulate probability of out-board.
                    else:
                        out_board_p += prob * 0.125
            memo = next_memo
        # the on-board prob = 1 - the accumulate out board prob
        return 1-out_board_p


"""

问题分析：
  这个是今天同学阿里内推笔试题目，我拿到题目的第一眼望去，就是深度优先搜索，回溯法，真是太年轻了，
这个用回溯法的话，复杂度会非常高，因为路径应该是可以重复走的，可能性路径就更多了。
后天面试官提示是动态规划，才开始考虑k这个因素。 
   动态规划解法：

令 f[r][c][steps]表示， 经过steps步之后落在棋盘(r, c) 上的概率。则dp递推方程如下： 
f[r][c][steps]=∑dr,dcf[ri+dr][cj+dc][steps−1]/8
f[r][c][steps]=∑dr,dcf[ri+dr][cj+dc][steps−1]/8

dr, dc 表示下一步要走的偏量，且r = ri+dr，c = cj+dc，也就是，只要在steps-1的步骤中，
所有可能的位置到达steps步骤中的(r, c)，的概率总和，就是steps步骤中(r, c)的概率。
最后只要求出在最后一步棋盘上所有位置上概率的总和就是题目要求的结果。
问题：为什么要除以8？因为每次有八分之一的概率选择一个方向，也就是每个位置被选择的概率是1/8。
问题：出界的概率怎么办？这个不用考虑，因为，只求界内的概率，所以不用考虑出界的概率。
现在看看优化问题，很显然，在每一个steps步骤中，只需要当前步骤steps的数据，和前一个steps-1的数据，
就可以完成计算，所以f[r][c][steps] 这个3维数组，完全可以用两个2维数组代替。 
所以用，dp2表示 f[][][steps]，用dp表示f[][][steps-1]
"""
class Solution5:
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]  # 初始化dp
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]  # 初始化当前dp
            for r in range(N):
                for c in range(N):
                    for dr, dc in zip((2, 2, -2, -2, 1, 1, -1, -1), (1, -1, 1, -1, 2, -2, 2, -2)):  # 八个方向
                        if 0 <= r + dr < N and 0 <= c + dc < N:  # 判断是否出界
                            dp2[r+dr][c+dc] += dp[r][c] / 8.0  # 保留棋盘内的概率（除以8，是因为有八个方向，每个方向是八分之一）
            dp = dp2  # 更新steps-1步骤中的棋盘概率数据
        return sum(map(sum, dp))  # 把落在棋盘上的所有位置的概率加起来，就是最后落在棋盘上的概率


"""
解题思路：
动态规划（Dynamic Programming）

利用字典dmap存储骑士落在棋盘某位置的概率。

dmap[(nx, ny)] += dmap[(x, y)] * 0.125
其中(x, y)为当前位置，(nx, ny)为下一个位置
"""
class Solution6:
    def knightProbability(self, N, K, r, c):

        dxs = [-2, -2, -1, -1, 1, 1, 2, 2]
        dys = [-1, 1, -2, 2, -2, 2, -1, 1]
        ans = 0
        dmap = {(r, c) : 1}
        for t in range(K):
            dmap0 = collections.defaultdict(int)
            for (x, y), pb in dmap.iteritems():
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        ans += 0.125 * pb
                    else:
                        dmap0[(nx, ny)] += 0.125 * pb
            dmap = dmap0
        return 1 - ans

#GeeksforGeeks
# size of the chessboard
N = 8

# Direction vector for the Knight
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


# returns true if the knight
# is inside the chessboard
def inside(x, y):
    return (x >= 0 and x < N and y >= 0 and y < N)


# Bottom up approach for finding the
# probability to go out of chessboard.
def findProb(start_x, start_y, steps):
    # dp array
    dp1 = [[[0 for i in range(N + 1)]
            for j in range(N + 1)]
           for k in range(N + 1)]

    # For 0 number of steps, each
    # position will have probability 1
    for i in range(N):

        for j in range(N):
            dp1[i][j][0] = 1

    # for every number of steps s
    for s in range(1, steps + 1):

        # for every position (x,y) after
        # s number of steps
        for x in range(N):

            for y in range(N):
                prob = 0.0

                # For every position reachable from (x,y)
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # if this position lie inside the board
                    if (inside(nx, ny)):
                        prob += dp1[nx][ny][s - 1] / 8.0

                # store the result
                dp1[x][y][s] = prob

                # return the result
    return dp1[start_x][start_y][steps]


# Driver code

# number of steps
K = 3
print(findProb(0, 0, K))


