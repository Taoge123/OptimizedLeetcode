"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""


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




