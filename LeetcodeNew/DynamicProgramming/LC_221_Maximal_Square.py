
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
"""
dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1.
"""

"""
221. Maximum Square
> 类型：二维DP
> Time Complexity O(N^2)
> Space Complexity O(N^2)
画了个图，大家意会哈。
"""
class Solution1:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0

        res = max(max(row) for row in dp)
        return res ** 2

"""
We define dp[i][j] the maximal ending at position (i, j). 
Thus, current state (dp[i][j])depends on left (dp[i][j - 1]), up (dp[i - 1][j]), 
and left-up's (dp[i - 1][j - 1]) states. The current state equals to the minimum of these three states plus matrix[i][j] 
because any smaller value will lead to a smaller square (holes in somewhere). 
I use maxArea to track the maximal square. When matrix[i][j] == '0', the maximal square ending at position (i, j) is obviously 0.

Recurrence relation:

For matrix[i][j] == 1, dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + int(matrix[i][j]).

For matrix[i][j] == 0, dp[i][j] = 0
"""
class Solution2:
    def maximalSquare(self, matrix):
        dp, maxArea = [[0 for _1_ in range(len(matrix[0]))] for ___ in range(len(matrix))], 0
        for i in xrange(0, len(matrix)):
            for j in xrange(0, len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                maxArea = max(maxArea, dp[i][j])
        return maxArea * maxArea


class Solution3:
    # O((m+1)*(n+1)) space, one pass
    def maximalSquare1(self, matrix):
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0 for i in xrange(c + 1)] for j in xrange(r + 1)]
        res = 0
        for i in xrange(r):
            for j in xrange(c):
                dp[i + 1][j + 1] = (min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1) * int(matrix[i][j])
                res = max(res, dp[i + 1][j + 1] ** 2)
        return res

    # O(m*n) space, one pass
    def maximalSquare2(self, matrix):
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in xrange(c)] for i in xrange(r)]
        res = max(max(dp))
        for i in xrange(1, r):
            for j in xrange(1, c):
                dp[i][j] = (min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1) * int(matrix[i][j])
                res = max(res, dp[i][j] ** 2)
        return res

    # O(2*n) space
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        pre = cur = [0] * (c + 1)
        res = 0
        for i in xrange(r):
            for j in xrange(c):
                cur[j + 1] = (min(pre[j], pre[j + 1], cur[j]) + 1) * int(matrix[i][j])
                res = max(res, cur[j + 1] ** 2)
            pre = cur
            cur = [0] * (c + 1)
        return res

"""
Let f(i, j) be the size of possible largest full-1-square of the grid with index (i, j) being the bottom-right index. 
When i == 0, f(i, j) is at most 1, and it equals to the corresponding number in matrix[i, j]; 
similarly when j == 0. For general i, j, f(i, j) = min(f(i-1, j), f(i, j-1), f(i-1, j-1)) + 1 if matrix[i, j] == '1' otherwise 0. 
The desired result is d ** 2 where d = the maximal number in the matrix f(i, j).
"""
class Solution4:
    def maximalSquare(self, matrix):

        if not matrix: return 0
        d = 0
        m, n = len(matrix), len(matrix[0])
        f = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
                d = max(d, f[i][j])
        return d**2


class Solution44:
    def maximalSquare(self, matrix):

        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        for j in range(n):
            f[0][j] = int(matrix[0][j])
        for i in range(1, m):
            f[i][0] = int(matrix[i][0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])

        d = max(f[i][j] for i in range(m) for j in range(n))
        return d ** 2

"""
[1 if ch == '1' else 0 for ch in row] can be much shorter.
map(int, row)
"""





