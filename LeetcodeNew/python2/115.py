
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         m, n = len(s) + 1, len(t) + 1
#         dp = [[1] * n for i in range(m)]
#         for j in range(1, n):
#             dp[0][j] = 0
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i-1][j] + dp[i-1][j-1] * (s[i-1] == t[j-1])
#         return dp[-1][-1]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s) + 1, len(t) + 1
        cur = [0] * n
        cur[0] = 1
        for i in range(1, m):
            pre = cur[:]
            for j in range(1, n):
                cur[j] = pre[j] + pre[j - 1] * (s[i - 1] == t[j - 1])
        return cur[-1]




