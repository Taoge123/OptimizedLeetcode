"""
https://leetcode-cn.com/problems/number-of-paths-with-max-score/solution/jian-dan-ji-yi-hua-di-gui-jin-xing-dong-tai-gui-hu/

https://www.youtube.com/watch?v=WwdjLkWmDPs

"""

import functools

class SolutionTD:
    def pathsWithMaxScore(self, board):
        mod = 10 ** 9 + 7
        m, n = len(board), len(board[0])

        @functools.lru_cache(None)
        def dfs(i, j, count):
            if i == 0 and j == 0:
                return [0, 1]

            if i < 0 or j < 0 or board[i][j] == "X":
                return [-float("inf"), -float("inf")]

            count = 0
            if board[i][j] != "S":
                val = int(board[i][j])
            else:
                val = 0

            m1, c1 = dfs(i - 1, j, count + 1)
            m2, c2 = dfs(i, j - 1, count + 1)
            m3, c3 = dfs(i - 1, j - 1, count + 1)
            max_length = max(m1, m2, m3)

            for m, c in ((m1, c1), (m2, c2), (m3, c3)):
                if m == max_length:
                    count += c

            return [max_length + val, count]

        a, b = dfs(m - 1, n - 1, 0)
        return [a % mod, b % mod] if a != -float("inf") or b != -float("inf") else [0, 0]



class Solution:
    def pathsWithMaxScore(self, board):
        if not board:
            return [0, 0]
        n = len(board)
        mod = 10 ** 9 + 7
        # dp[i][j][0] is the max value from 'S' to this cell
        # dp[i][j][1] is the number of paths
        dp = [[[-1, 0] for i in range(n + 1)] for j in range(n + 1)]
        dp[0][0] = [0, 0]
        dp[n - 1][n - 1] = [0, 1]

        for i in range(n)[::-1]:
            for j in range(n)[::-1]:
                if board[i][j] in 'XS':
                    continue
                for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                    x = i + dx
                    y = j + dy
                    if dp[i][j][0] < dp[x][y][0]:
                        dp[i][j] = [dp[x][y][0], 0]

                    if dp[i][j][0] == dp[x][y][0]:
                        dp[i][j][1] += dp[x][y][1]
                        dp[i][j][1] %= mod

                # if there exits some path from 'E' to current position, update info of current position
                if dp[i][j][0] != -1 and (i or j):
                    dp[i][j][0] += int(board[i][j])
                    dp[i][j][0] %= mod

        return dp[0][0]




