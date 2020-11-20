

"""
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""

"""
dp[i][j] : the minimum number if steps required to make word[0:i] and word[0:j] the same
dp[i][j]
dp[i-1][j]
dp[i][j-1]

X X X X X X X X i
Y Y Y Y Y Y Y Y Y j

if i == j:
    dp[i-1][j-1]
else:
    dp[i-1][j], dp[i][j-1]


"""

import functools


class SolutionDFS1:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m and j == m:
                return 0

            if i == m or j == n:
                return m - i or n - j

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j + 1)) + 1

        return dfs(0, 0)


class SolutionDFS2:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.dfs(word1, word2, 0, 0, memo)

    def dfs(self, word1, word2, i, j, memo):
        m, n = len(word1), len(word2)
        if (i, j) in memo:
            return memo[(i, j)]

        if i == m and j == n:
            return 0

        if i == m or j == n:
            return m - i or n - j

        if word1[i] == word2[j]:
            res = self.dfs(word1, word2, i + 1, j + 1, memo)
        else:
            res = min(self.dfs(word1, word2, i + 1, j, memo), self.dfs(word1, word2, i, j + 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]





class SolutionTony:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) or len(word2)

        m, n = len(word1), len(word2)
        dp = [[float('inf') for j in range(n + 1)] for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], min(dp[i - 1][j], dp[i][j - 1]) + 1)

        return dp[m][n]



class SolutionDP:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[m][n]




class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for i in range(m+1)]

        for i in range(m):
            dp[i][-1] = m - i
        for j in range(n):
            dp[-1][j] = n - j

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]




class Solution4:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)

        for i in range(m + 1):
            temp = [0] * (n + 1)
            for j in range(n + 1):
                if i == 0 or j == 0:
                    temp[j] = i + j
                elif (word1[i - 1] == word2[j - 1]):
                    temp[j] = dp[j - 1]
                else:
                    temp[j] = 1 + min(dp[j], temp[j - 1])
            dp = temp

        return dp[n]




word1 = "sea"
word2 = "eat"

a = Solution2()
print(a.minDistance(word1, word2))
