"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""
import functools


class SolutionTonyTD:
    def minCut(self, s: str) -> int:
        dp = {}
        self.isPal(s, 0, len(s) - 1, dp)
        memo = {}
        return self.dfs(s, 0, dp, memo) - 1


    def isPal(self, s, i, j, dp):  # l, r inclusive
        if (i, j) in dp:
            return dp[(i, j)]
        if i >= j:
            return True
        if s[i] != s[j]:
            return False
        if self.isPal(s, i + 1, j - 1, dp):
            dp[(i, j)] = True
            return True
        dp[(i, j)] = False
        return False

    def dfs(self, s, i, dp, memo):  # s[i..n-1]
        if i in memo:
            return memo[i]
        n = len(s)
        if i == n:
            return 0
        res = float('inf')
        for j in range(i, n):
            if (self.isPal(s, i, j, dp)):
                res = min(res, self.dfs(s, j + 1, dp, memo) + 1)
        memo[i] = res
        return res



class SolutionTD:
    def minCut(self, s: str) -> int:
        n = len(s)

        @functools.lru_cache(None)
        def isPal(l, r):  # l, r inclusive
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return isPal(l + 1, r - 1)

        @functools.lru_cache(None)
        def dfs(i):  # s[i..n-1]
            if i == n:
                return 0
            res = float('inf')
            for j in range(i, n):
                if (isPal(i, j)):
                    res = min(res, dfs(j + 1) + 1)
            return res

        return dfs(0) - 1

class Solution:
    def minCut(self, s: str) -> int:

        dp = [-1] + [len(s) - 1 for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                temp = s[i:j]
                if s[i:j] == s[i:j][::-1]:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]


class Solution2:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        isPalindrome = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i] = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or isPalindrome[j + 1][i - 1]):
                    isPalindrome[j][i] = True
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
        return dp[n - 1]


"""
dp[i] : minimum cuts needed for a palindrome partitioning of s
X X X X X X X [j X i]

dp[i] = min(dp[j] + 1 if s[j:i] == s[j:i][::-1] for every j)
"""


class SolutionWisdom1:
    def minCut(self, s: str) -> int:

        n = len(s)
        dp = [float('inf') for i in range(n)]
        dp[0] = 1
        for i in range(1, n):
            for j in range(i + 1):
                if self.isPal(s, j, i):
                    if j == 0:
                        dp[i] = 1

                    else:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1] - 1

    def isPal(self, s, i, j):
        return s[i:j + 1] == s[i:j + 1][::-1]


s = "aab"
a = Solution2()
print(a.minCut(s))



