"""
LCS - Longest Common Subsequence


"""


class Solution:
    def minScoreTriangulation(self, A) -> int:
        n = len(A)
        dp = [[0 for i in range(n)] for j in range(n)]

        for step in range(2, n):
            for i in range(n - step):
                j = i + step
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + A[i] * A[j] * A[k] + dp[k][j])

        return dp[0][n - 1]


class SolutionWisdom:
    def minScoreTriangulation(self, A) -> int:
        n = len(A)
        dp = [[float('inf') for i in range(n)] for j in range(n)]

        for i in range(n - 1):
            dp[i][i + 1] = 0

        for step in range(3, n + 1):
            for i in range(n - step + 1):
                j = i + step - 1
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + A[i] * A[k] * A[j] + dp[k][j])

        return dp[0][n - 1]


class SolutionTD:
    def minScoreTriangulation(self, A) -> int:
        A = A
        n = len(A)
        cache = [[0 for i in range(n)] for j in range(n)]

        return self.dfs(A, 0, n - 1, cache)

    def dfs(self, nums, i, j, cache):
        if i >= j or j == i + 1:
            return 0
        if cache[i][j]:
            return cache[i][j]

        res = float('inf')
        for k in range(i + 1, j):
            res = min(res, nums[i] * nums[j] * nums[k] + self.dfs(nums, i, k, cache) + self.dfs(nums, k, j, cache))

        cache[i][j] = res
        return res







