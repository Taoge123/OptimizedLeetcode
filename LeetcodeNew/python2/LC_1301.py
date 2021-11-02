"""
https://leetcode-cn.com/problems/number-of-paths-with-max-score/solution/jian-dan-ji-yi-hua-di-gui-jin-xing-dong-tai-gui-hu/

https://www.youtube.com/watch?v=WwdjLkWmDPs

"""

import functools


class SolutionTD1:  # top down dp1
    def pathsWithMaxScore(self, board):
        # 下棋，从右下角S出发 到左上角E结束，可以往上走，往左走，左斜走。
        # return 最大sum 和 几种方式可以得到最大sum
        # 类似题 673. Number of Longest Increasing Subsequence

        # dfs --> 同时分别求 最大sum 和 几种方式
        memo = {}
        maxval, count = self.dfs(board, len(board) - 1, len(board[0]) - 1, memo)
        mod = 10 ** 9 + 7
        if maxval != float('-inf'):
            return [maxval % mod, count % mod]
        else:
            return [0, 0]

    def dfs(self, board, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # over the range
        if i < 0 or j < 0 or board[i][j] == 'X':
            return float('-inf'), 0
        # base case
        if i == 0 and j == 0 and board[i][j] == 'E':
            return 0, 1

        # recursive
        v1, c1 = self.dfs(board, i, j - 1, memo)
        v2, c2 = self.dfs(board, i - 1, j, memo)
        v3, c3 = self.dfs(board, i - 1, j - 1, memo)
        maxval = max(v1, v2, v3)

        count = 0
        for x, y in ((v1, c1), (v2, c2), (v3, c3)):
            if x == maxval:
                count += y

        if board[i][j] != 'S':
            val = int(board[i][j])
        else:
            val = 0

        memo[(i, j)] = maxval + val, count
        return memo[(i, j)]



class SolutionTD2:  # top down dp2
    def pathsWithMaxScore(self, board):

        memo = {}
        maxval, count = self.dfs(board, len(board) - 1, len(board[0]) - 1, memo)
        mod = 10 ** 9 + 7
        if maxval != float('-inf'):
            return [maxval % mod, count % mod]
        else:
            return [0, 0]

    def dfs(self, board, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i < 0 or j < 0 or board[i][j] == 'X':
            return float('-inf'), 0

        if i == 0 and j == 0 and board[i][j] == 'E':
            return 0, 1

        if board[i][j] != 'S':
            cur_val = int(board[i][j])
        else:
            cur_val = 0

        maxval = float('-inf')
        count = 0
        for dx, dy in ((0, -1), (-1, 0), (-1, -1)):
            # 为什么不在dfs后面直接加board[i][j] --->因为dfs返回是两个值，count是不能加board[i][j]DE
            val, cnt = self.dfs(board, i + dx, j + dy, memo)

            if val + cur_val > maxval:
                maxval = val + cur_val
                count = cnt
            elif val + cur_val == maxval:
                count += cnt

        memo[(i, j)] = maxval, count
        return memo[(i, j)]


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




