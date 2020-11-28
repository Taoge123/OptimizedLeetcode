"""

Longest Common Sequence

Have you ever heard the problem:
Find out the longest common sequence.
Similar problem: 1035. Uncrossed Lines


https://www.youtube.com/watch?v=Zj871uqXadE
"""
"""
X X X X X i
Y Y Y Y j


dp[i][j] : the maximum dot product between non-empty subsequeences of nums1[0:i] and nums2[0:j] with the same length

1. A[i]*B[j] -> dp[i][j] = max(dp[i-1][j-1] + A[i]*B[j], 0)
2. do not pair A[i], B[j] -> dp[i][j] = max(dp[i][j-1], dp[i-1][j])



"""

import functools

class SolutionDFS1:
    def maxDotProduct(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)
        @functools.lru_cache(None)
        def dfs(i, j):
            # if i == m and j == n:
            #     return 0
            if i == m or j == n:
                return float('-inf')

            res = float('-inf')
            # pick cur and prev, pick cur and abandon prev, i move or j move
            res = max(dfs(i + 1, j + 1) + nums1[i] * nums2[j], nums1[i] * nums2[j], dfs(i + 1, j), dfs(i, j + 1))
            return res

        return dfs(0, 0)



class SolutionDFS2:
    def maxDotProduct(self, nums1, nums2) -> int:
        memo = {}
        return self.dfs(nums1, nums2, 0, 0, memo)

    def dfs(self, nums1, nums2, i, j, memo):
        m, n = len(nums1), len(nums2)
        if (i, j) in memo:
            return memo[(i, j)]

        if i == m or j == n:
            return float('-inf')

        # pick cur and prev, pick cur and abandon prev, i move or j move
        res = max(self.dfs(nums1, nums2, i + 1, j + 1, memo) + nums1[i] * nums2[j],
                  nums1[i] * nums2[j],
                  self.dfs(nums1, nums2, i + 1, j, memo),
                  self.dfs(nums1, nums2, i, j + 1, memo))
        memo[(i, j)] = res
        return res



class SolutionTony:
    def maxDotProduct(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf') for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1])
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]





class Solution:
    def maxDotProduct(self, nums1, nums2) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m) for i in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = nums1[i] * nums2[j]
                if i and j:
                    dp[i][j] += max(dp[i - 1][j - 1], 0)
                if i:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]




