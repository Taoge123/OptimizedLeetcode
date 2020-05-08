
"""
873. Length of Longest Fibonacci Subsequence

"""
import collections

class Solution:
    def longestArithSeqLength(self, A) -> int:
        # dp[i, diff] = length
        dp = {}
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                dp[j, diff] = dp.get((i, diff), 1) + 1
        return max(dp.values())


class SolutionTLE:
    def longestArithSeqLength(self, A) -> int:
        # dp[i, diff] = length
        self.cache = collections.defaultdict(dict)
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                res = max(res, self.dfs(A, i, diff) + 2)

        return res

    def dfs(self, A, i, diff):
        if i < 0:
            return 0

        if self.cache.get(i) != None and diff in self.cache.get(i):
            return self.cache[i][diff]

        res = 0
        for j in range(i - 1, -1, -1):
            if A[i] - A[j] == diff:
                res = max(res, 1 + self.dfs(A, j, diff))

        self.cache[i][diff] = res
        return self.cache[i][diff]







