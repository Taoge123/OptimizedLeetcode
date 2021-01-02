"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/413054/ALL-4-ways-Recursion-greater-Top-down-greaterBottom-Up-including-VIDEO-TUTORIAL

longest common subarray
dp[i][j] => dp[i-1][j-1] if A[i]==B[j] else 0

longest common subsequence (LCS) : DP
dp[i][j] => dp[i-1][j-1] if A[i]==B[j] else min(dp[i][j-1], dp[i-1][j])

dp[i][j]: the longest common subarray that ends at A[i] and ends at B[j]

XXX[XX i]
YYYYY[YYY j]

dp[i][j] => dp[i-1][j-1] if A[i]==B[j] else 0

"""



class Solution:
    def findLength(self, A, B) -> int:
        m, n = len(A), len(B)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
        return res

