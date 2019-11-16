
"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        bbbab
        [1, 2, 3, 3, 4]
        [0, 1, 2, 2, 3]
        [0, 0, 1, 1, 3]
        [0, 0, 0, 1, 1]
        [0, 0, 0, 0, 1]
        """
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]









