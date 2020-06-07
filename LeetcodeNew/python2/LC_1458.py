"""

Longest Common Sequence

Have you ever heard the problem:
Find out the longest common sequence.
Similar problem: 1035. Uncrossed Lines


https://www.youtube.com/watch?v=Zj871uqXadE
"""

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




