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




