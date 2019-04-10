
"""
https://leetcode.com/problems/longest-palindromic-subsequence/discuss/227765/Python-Recursive-Memorisation-beats-90

Given a string s, find the longest palindromic subsequence's length in s.
You may assume that the maximum length of s is 1000.

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

"""
dp[i][j]: the longest palindromic subsequence's length of substring(i, j), 
here i, j represent left, right indexes in the string
State transition:
dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
Initialization: dp[i][i] = 1
"""
"""
Idea:
dp[i][j] = longest palindrome subsequence of s[i to j].
If s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
Else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
Rolling array O(2n) space
"""

class Solution1:
    def longestPalindromeSubseq(self, s):

        n = len(s)
        dp = [[1] * 2 for _ in range(n)]
        for j in range(1, len(s)):
            for i in reversed(range(0, j)):
                if s[i] == s[j]:
                    dp[i][j%2] = 2 + dp[i + 1][(j - 1)%2] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j%2] = max(dp[i + 1][j%2], dp[i][(j - 1)%2])
        return dp[0][(n-1)%2]

# Further improve space to O(n)
class Solution2:
    def longestPalindromeSubseq(self, s):

        n = len(s)
        dp = [1] * n
        for j in range(1, len(s)):
            pre = dp[j]
            for i in reversed(range(0, j)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]


"""
I found that for python, the standard DP solutions (time O(n^2), 
space O(n^2)) might get TLE, while the O(n) space solutions can get accepted in ~1400ms.

But if we simply check if s itself is a palindrome first, 
we could reduce a lot of unnecessary dp steps to speed it up.

This space O(n) DP solution got accepted in 619 ms, beating 100%."""

class Solution3:
    def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [0 for j in range(n)]
        dp[n - 1] = 1

        for i in range(n - 1, -1, -1):  # can actually start with n-2...
            newdp = dp[:]
            newdp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j - 1]
                else:
                    newdp[j] = max(dp[j], newdp[j - 1])
            dp = newdp

        return dp[n - 1]


# This standard dp solution (space O(n2) with the same trick got accepted in ~900 ms
class Solution4:
    def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]








