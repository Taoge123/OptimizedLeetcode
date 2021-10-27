
"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.



Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:



Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
"""

import collections
import functools

class SolutionTony:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:

        mod = 10 ** 9 + 7
        @functools.lru_cache(None)
        def dfs(i, j, steps):
            # Reach the target
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1

                # No step left
            if steps == 0:
                return 0

            # Heuristic: Not enough steps left to go out of any boundary
            # if (m-i > steps and n-sj > steps and i+1 > steps and sj+1 > steps):
            #     return 0
            res = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                res += dfs(x, y, steps - 1)
            return res

        return dfs(i, j, N) % mod



class SolutionTLE:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        mod = 10 ** 9 + 7
        queue = collections.deque([(i, j, 0)])
        res = 0
        while queue:
            x, y, step = queue.popleft()
            if step > N:
                break
            if 0 <= x < m and 0 <= y < n:
                queue.append((x + 1, y, step + 1))
                queue.append((x - 1, y, step + 1))
                queue.append((x, y + 1, step + 1))
                queue.append((x, y - 1, step + 1))
            else:
                res += 1
        return res % mod



class Solution1:
    def findPaths(self, m, n, N, i, j):
        memo = {}
        self.MOD = 10 ** 9 + 7
        return self.helper(N, i, j, m, n, memo) % self.MOD

    def helper(self, N, i, j, m, n, memo):
        if (N, i, j) in memo:
            return memo[(N, i, j)]
        if N == 0:
            return 0
        res = 0
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n:
                res += self.helper(N - 1, i + x, j + y, m, n, memo)
            else:
                res += 1
        memo[(N, i, j)] = res
        return res


class Solution2:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:

        dp = [[0] * n for i in range(m)]
        mod = 10 ** 9 + 7
        for k in range(1, N + 1):
            newDP = [[0 for i in range(n)] for j in range(m)]
            for x in range(m):
                for y in range(n):
                    a = 1 if x == 0 else dp[x - 1][y]
                    b = 1 if x == m - 1 else dp[x + 1][y]
                    c = 1 if y == 0 else dp[x][y - 1]
                    d = 1 if y == n - 1 else dp[x][y + 1]
                    newDP[x][y] = (a + b + c + d) % mod

            dp = newDP

        return dp[i][j]


class Solution3:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:

        MOD = 10 ** 9 + 7
        nxt = [[0] * n for _ in range(m)]
        nxt[i][j] = 1

        res = 0
        for step in range(N):
            dp = nxt
            nxt = [[0] * n for _ in range(m)]
            for i, row in enumerate(dp):
                for j, val in enumerate(row):
                    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= x < m and 0 <= y < n:
                            nxt[x][y] += val
                            nxt[x][y] %= MOD
                        else:
                            res += val
                            res %= MOD

        return res







