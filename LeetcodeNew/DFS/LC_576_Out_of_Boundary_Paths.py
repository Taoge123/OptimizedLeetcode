"""



There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball,
you can move the ball to adjacent cell
or cross the grid boundary in four directions (up, down, left, right).
However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary.
The answer may be very large, return it after mod 109 + 7.



Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:



"""

#https://buptwc.com/2018/07/19/Leetcode-576-Out-of-Boundary-Paths/
"""
给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，
或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你最多可以移动N次。
找出可以将球移出边界的路径数量。答案可能非常大，返回结果mod 1e9+7的值。

分析：

这道题乍一看很像一个标准的bfs，因为限定最多只能移动N次，我们只要bfs依次遍历发现出界就+1，
当bfs的深度大于N的时候break。当然理论上是没有任何问题的，确实能得出正确答案，
但是这里N的取值范围达到了50，我们对任意一个点bfs有四个方向（可以走回头路），
那么复杂度达到了4^N，显然会超时。当然我会在文章后面给出bfs的做法，
毕竟这是可以处理N比较小的情况的解法，让大家更熟悉bfs的套路。
我不知道你们有没有这种感觉，一般看到这个mod 1e9+7，这道题8成就是dp了，
而且就是那种每个dp值你都得mod一下再去进行运算的那种。我觉得这算一个小技巧吧，
看到mod 1e9+7就要想到dp。
显然，这里dp很好定义，我们定义dp[(i,j,N)]表示从i,j出发，最多走N步情况下满足题意的路径数量，
那么我们所求也就是dp[(i,j,N)]。根据我们上面说的bfs的思路，递推式可得：

dp[(i,j,N)] = dp[(i+1,j,N-1)] + dp[(i-1,j,N-1)] + dp[(i,j+1,N-1)] + dp[(i,j-1,N-1)]

思路：
处理好边界情况：
当i,j仍然在网格内时，如果N=0，说明这条路走不出去,dp[(i,j,N)] = 0
当i,j仍然在网格内时，如果N>0，如递推式
当i,j在网格外时，说明已经走出去，dp[(i,j,N)] = 1
这里我为了方便代码书写就用的记忆化的形式，用一个cache来存储已经计算过的结果

"""
import collections

class Solution(object):
    def findPaths(self, m, n, N, i, j):
        mod = 10**9 + 7
        cache = collections.defaultdict(int)
        def helper(i,j,N):
            # 记忆化思想
            if (i,j,N) in cache:
                return cache[(i,j,N)]
            #i,j在网格内情况
            if 0<=i<m and 0<=j<n:
                if N == 0:
                    cache[(i,j,N)] = 0
                    return cache[(i,j,N)]

                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    cache[(i,j,N)] += helper(x,y,N-1)
                return cache[(i,j,N)] % mod
            # 网格外情况
            else:
                cache[(i,j,N)] = 1
                return cache[(i,j,N)]
        return helper(i,j,N) % mod


class Solution2:
    def findPaths(self, R, C, N, sr, sc):
        MOD = 10 ** 9 + 7
        nxt = [[0] * C for _ in range(R)]
        nxt[sr][sc] = 1

        ans = 0
        for time in range(N):
            cur = nxt
            nxt = [[0] * C for _ in range(R)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < R and 0 <= nc < C:
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= MOD
                        else:
                            ans += val
                            ans %= MOD

        return ans

class Solution3:
    def findPaths(self, m, n, N, x, y):
        M = [[0 for i in range(n)] for j in range(m)]
        for _ in range(N):
            M = [[(i == 0 or M[i - 1][j]) + (i + 1 == m or M[i + 1][j])
                  + (j == 0 or M[i][j - 1]) + (j + 1 == n or M[i][j + 1])
                  for j in range(n)] for i in range(m)]
        return M[x][y] % (10 ** 9 + 7)


class Solution4:
    def __init__(self): self.dic = collections.defaultdict(int)
    def findPaths(self, m, n, N, i, j):
        if N >= 0 and (i < 0 or j < 0 or i >= m or j >= n): return 1
        elif N < 0: return 0
        elif (i, j, N) not in self.dic:
            for p in ((1, 0), (-1, 0), (0, 1), (0, -1)): self.dic[(i, j, N)] += self.findPaths(m, n, N - 1, i + p[0], j + p[1])
        return self.dic[(i, j, N)] % (10 ** 9 + 7)




class Solution5:
    def findPaths(self, m, n, N, i, j):
        d = [[[-1] * n for _ in range(m)] for _ in range(N + 1)]
        def dfs(N, i, j, d):
            if i in [-1, m] or j in [-1, n]:
                return 1
            if N == 0:
                return 0
            if d[N][i][j] != -1:
                return d[N][i][j]
            d[N][i][j] = dfs(N - 1, i - 1, j, d) + dfs(N - 1, i + 1, j, d) + dfs(N - 1, i, j - 1, d) + dfs(N - 1,i, j + 1, d)
            return d[N][i][j] % (10**9 + 7)
        return dfs(N, i, j, d)










