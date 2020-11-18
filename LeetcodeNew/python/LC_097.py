"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false



"""

import functools

class SolutionDFS1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        return self.dfs(0, 0, 0, s1, s2, s3, memo)

    def dfs(self, i, j, k, s1, s2, s3, memo):
        m, n, o = len(s1), len(s2), len(s3)
        if i == m and j == n and k == o:
            return True

        if (i == m or j == n) and k == o:
            return False

        if (i, j) in memo:
            return memo[(i, j)]

        res = False
        if i < len(s1) and j < len(s2) and s1[i] == s2[j] and s2[j] == s3[k]:
            res = self.dfs(i + 1, j, k + 1, s1, s2, s3, memo) or self.dfs(i, j + 1, k + 1, s1, s2, s3, memo)

        elif i < len(s1) and s1[i] == s3[k]:
            res = self.dfs(i + 1, j, k + 1, s1, s2, s3, memo)

        elif j < len(s2) and s2[j] == s3[k]:
            res = self.dfs(i, j + 1, k + 1, s1, s2, s3, memo)

        memo[(i, j)] = res
        return memo[(i, j)]


class SolutionDFS2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        @functools.lru_cache(None)
        def dfs(i, j, k, s1, s2, s3):
            m, n, o = len(s1), len(s2), len(s3)
            if i == m and j == n and k == o:
                return True

            if (i == m or j == n) and k == o:
                return False

            if i < len(s1) and j < len(s2) and s1[i] == s2[j] and s2[j] == s3[k]:
                return dfs(i + 1, j, k + 1, s1, s2, s3) or dfs(i, j + 1, k + 1, s1, s2, s3)

            elif i < len(s1) and s1[i] == s3[k]:
                return dfs(i + 1, j, k + 1, s1, s2, s3)

            elif j < len(s2) and s2[j] == s3[k]:
                return dfs(i, j + 1, k + 1, s1, s2, s3)

        return dfs(0, 0, 0, s1, s2, s3)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        dp = [[True for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        dp = [True for i in range(n+1)]
        for j in range(1, n+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1]







s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
a = SolutionDFS1()
print(a.isInterleave(s1, s2, s3))




