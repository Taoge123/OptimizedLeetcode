"""
712.Minimum-ASCII-Delete-Sum-for-Two-Strings
对于此类有两个字符串、求最终使得彼此相同的操作的题目，一个典型的DP算法套路就是：设置状态数组dp[i][j]，
代表s1前i个字符、s2前j个字符时的目标值。考虑dp[i][j]和dp[i-1][j-1]、dp[i-1][j]、dp[i][j-1]的递推关系。

当s1[i]==s2[j]时，说明不需要删减任何字符，即能由状态(i-1,j-1)到(i,j)，即 dp[i][j]==dp[i-1][j-1]。

当s1[i]!=s2[j]时，可以从状态(i-1, j)通过删减s1[i]到(i,j)，
               或者才从状态(i, j-1)通过删减s2[j]到(i,j)，
所以 dp[i][j]= min(dp[i-1][j]+s1[i], dp[i][j-1]+s2[j])

另外需要特别注意边界条件dp[0][j]和dp[i][0]。

类似此题的还有：583 Delete Operation for Two Strings，97 Interleaving String，72 Edit Distance

Leetcode Link
"""

import functools


class SolutionTony:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        return self.dfs(s1, s2, 0, 0, memo)

    def dfs(self, s1, s2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(s1), len(s2)
        # if i == m and j == n:
        #     return 0

        if i == m or j == n:
            return sum([ord(i) for i in s1[i:]]) or sum([ord(i) for i in s2[j:]])

        # res = float('inf')
        if s1[i] == s2[j]:
            res = self.dfs(s1, s2, i + 1, j + 1, memo)
        else:
            res = min(self.dfs(s1, s2, i + 1, j, memo) + ord(s1[i]), self.dfs(s1, s2, i, j + 1, memo) + ord(s2[j]))
        memo[(i, j)] = res
        return memo[(i, j)]



class Solution2:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m or j == n:
                return sum([ord(i) for i in s1[i:]]) or sum([ord(i) for i in s2[j:]])

            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1)

            else:
                return min(dfs(i + 1, j) + ord(s1[i]), dfs(i, j + 1) + ord(s2[j]))

        return dfs(0, 0)




class Solution:
    def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i + j == 0:
                    continue
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + ord(s2[j - 1])
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + ord(s1[i - 1])
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

        return dp[m][n]




