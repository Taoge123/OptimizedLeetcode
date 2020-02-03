


"""
https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step.

"""

import collections

class SolutionTLE:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.helper(text1, text2, 0, 0)

    def helper(self, text1, text2, i, j):
        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            return self.helper(text1, text2, i + 1, j + 1) + 1

        return max(self.helper(text1, text2, i + 1, j), self.helper(text1, text2, i, j + 1))


class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        return self.helper(text1, text2, 0, 0, memo)

    def helper(self, text1, text2, i, j, memo):
        if memo[i][j] == -1:

            if i == len(text1) or j == len(text2):
                memo[i][j] = 0

            elif text1[i] == text2[j]:
                memo[i][j] = self.helper(text1, text2, i + 1, j + 1, memo) + 1

            else:
                memo[i][j] = max(self.helper(text1, text2, i + 1, j, memo), self.helper(text1, text2, i, j + 1, memo))

        return memo[i][j]


class Solution11SlowerThanPreviousOne:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        memo = collections.defaultdict(int)

        return self.helper(text1, text2, 0, 0, memo)

    def helper(self, text1, text2, i, j, memo):
        if not memo[(i, j)]:

            if i == len(text1) or j == len(text2):
                memo[(i, j)] = 0

            elif text1[i] == text2[j]:
                memo[(i, j)] = self.helper(text1, text2, i + 1, j + 1, memo) + 1

            else:
                memo[(i, j)] = max(self.helper(text1, text2, i + 1, j, memo), self.helper(text1, text2, i, j + 1, memo))

        return memo[(i, j)]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for i in range( m +1)] for j in range( n +1)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[ i +1][ j +1] = dp[i][j] + 1
                else:
                    dp[ i +1][ j +1] = max(dp[i][ j +1], dp[ i +1][j])

        return dp[-1][-1]





