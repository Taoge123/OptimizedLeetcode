"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""
        if len(set(s)) == 1:
            return s
        n = len(s)

        dp = [[0] * n for i in range(n)]
        maxi = 0
        res = ""
        for i in range(n):
            dp[i][i] = 1
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) and ((i - j < 2) or dp[j + 1][i - 1])
                if dp[j][i] and maxi < i - j + 1:
                    maxi = i - j + 1
                    res = s[j:i + 1]

        return res if res else s[0]














