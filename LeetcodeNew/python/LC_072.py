"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

import functools

class SolutionDFS1:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.dfs(word1, word2, 0, 0, memo)

    def dfs(self, s1, s2, i, j, memo):
        m, n = len(s1), len(s2)
        # if i == m and j == n:
        #     return 0
        if i == m:
            return len(s2) - j

        if j == n:
            return len(s1) - i

        if (i, j) in memo:
            return memo[(i, j)]

        # res = float('inf')
        if s1[i] == s2[j]:
            res = self.dfs(s1, s2, i + 1, j + 1, memo)

        else:
            res = min(self.dfs(s1, s2, i, j + 1, memo),
                      self.dfs(s1, s2, i + 1, j, memo),
                      self.dfs(s1, s2, i + 1, j + 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]





class SolutionDFS2:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m:
                return len(s2) - j

            if j == n:
                return len(s1) - i

            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(dfs(i, j + 1),
                           dfs(i + 1, j),
                           dfs(i + 1, j + 1)) + 1

        return dfs(0, 0)




class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]






