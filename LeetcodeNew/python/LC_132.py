"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""


class Solution:
    def minCut(self, s: str) -> int:

        f = [-1] + [len(s) -1 for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1 ,len(s) +1):
                if s[i:j] == s[i:j][::-1]:
                    f[j] = min(f[j], f[i] + 1)
        return f[-1]


class Solution2:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        isPalindrome = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            mini = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or isPalindrome[j + 1][i - 1]):
                    isPalindrome[j][i] = True
                    if j == 0:
                        mini = 0
                    else:
                        mini = min(mini, dp[j - 1] + 1)
            dp[i] = mini
        return dp[n - 1]



