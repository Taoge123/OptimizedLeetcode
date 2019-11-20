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
        maxi, res = 0, 0

        dp = [[0] * n for i in range(n)]

        for j in range(n):
            dp[j][j] = 1
            for i in range(j):
                # print('[', i, ']', '[', j, ']', '+', '[',i+1,']', '[',j-1,']')
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
                if dp[i][j] and maxi < j - i + 1:
                    maxi = j - i + 1
                    res = s[i: j + 1]

        return res if res else s[0]


"""
[ 0 ] [ 1 ] + [ 1 ] [ 0 ]
[ 0 ] [ 2 ] + [ 1 ] [ 1 ]
[ 1 ] [ 2 ] + [ 2 ] [ 1 ]
[ 0 ] [ 3 ] + [ 1 ] [ 2 ]
[ 1 ] [ 3 ] + [ 2 ] [ 2 ]
[ 2 ] [ 3 ] + [ 3 ] [ 2 ]
[ 0 ] [ 4 ] + [ 1 ] [ 3 ]
[ 1 ] [ 4 ] + [ 2 ] [ 3 ]
[ 2 ] [ 4 ] + [ 3 ] [ 3 ]
[ 3 ] [ 4 ] + [ 4 ] [ 3 ]

[1, F, 1, F, F]
[0, 1, F, 1, F]
[0, 0, 1, F, F]
[0, 0, 0, 1, F]
[0, 0, 0, 0, 1]
"""



s = "babad"
a = Solution()
print(a.longestPalindrome(s))













