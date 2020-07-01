"""
Simple Knapsack problem, dp(i,k) = dp(j,k-1) + cost(s[j+1....i]) for j<i and j+1>=k-1.


"""
"""
https://www.youtube.com/watch?v=kD6ShM6jr3g&t=238s
"""


from functools import lru_cache
import math

"""
dp[i][k] : the minimum number of characters that you need to change to divide the string s[0:i] into k substrings that are palindromes


XXX [j XXX i] +> min{dp[j-1][k-1] + cost(s[j:i])} for j in 1, 2, 3, ..., i


"""


class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        n = len(s)
        dp = [[float('inf') for i in range(K + 1)] for j in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for k in range(1, min(i, K) + 1):
                for j in range(k, i + 1):
                    dp[i][k] = min(dp[i][k], dp[j - 1][k - 1] + self.cost(s, j - 1, i - 1))

        return dp[n][K]

    def cost(self, s, a, b):
        count = 0
        while a < b:
            if s[a] != s[b]:
                count += 1
            a += 1
            b -= 1
        return count


class Solution:
    def palindromePartition(self, s, K):
        n = len(s)
        def cost(i, j):
            count = 0
            while i < j:
                if s[i] != s[j]:
                    count += 1
                i += 1
                j -= 1
            return count

        dp = [[float('inf') for i in range(K + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = cost(0, i - 1)
            for k in range(1, K + 1):
                for j in range(1, i):
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + cost(j, i - 1))

        return dp[n][K]


class SolutionPython:
    def palindromePartition(self, s: str, k: int) -> int:
        @lru_cache(None)
        def cost(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return cost(i + 1, j - 1)
            else:
                return cost(i + 1, j - 1) + 1

        @lru_cache(None)
        def dp(i, k):
            if k == 1:
                return cost(0, i)
            if k == i + 1:
                return 0
            if k > i + 1:
                return float('inf')
            return min([dp(j, k - 1) + cost(j + 1, i) for j in range(i)])

        return dp(len(s) - 1, k)




class Solution11:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        self.memo = {}
        return self.dfs(s, 0, k)

    # calculate the cost of transferring one substring into palindrome string
    def cost(self, s, i, j):
        res = 0
        while i < j:
            if s[i] != s[j]:
                res += 1
            i += 1
            j -= 1
        return res

    def dfs(self, s, i, k):
        if (i, k) in self.memo:
            return self.memo[(i, k)]
        n = len(s)
        # base case that each substring just have one character
        if n - i == k:
            return 0
        # base case that need to transfer whole substring into palidrome
        if k == 1:
            return self.cost(s, i, n - 1)
        res = float('inf')
        # keep making next part of substring into palidrome
        for j in range(i + 1, n - k + 2):
            # compare different divisions to get the minimum cost
            res = min(res, self.dfs(s, j, k - 1) + self.cost(s, i, j - 1))
        self.memo[(i, k)] = res
        return res


class Solution2:
    def palindromePartition(self, s: str, k: int) -> int:
        self.mem = {}
        return self.dfs(s, k)

    def dfs(self, s, k):
        if (s, k) in self.mem:
            return self.mem[(s, k)]
        if len(s) == k:
            return 0
        if k == 1:
            res = sum([s[i] != s[-1-i] for i in range(len(s) // 2)])
        else:
            res = float("Inf")
            for i in range(1, len(s) - k + 2):
                res = min(self.dfs(s[:i], 1) + self.dfs(s[i:], k - 1), res)
        self.mem[(s, k)] = res
        return res



class Solution3:
    def palindromePartition(self, s: str, k: int) -> int:
        return self.dp(s, 0, k)

    @lru_cache(maxsize=None)
    def cost(self, s, i, j):
        res = 0
        while i < j:
            if s[i] != s[j]:
                res += 1
            i, j = i + 1, j - 1
        return res

    @lru_cache(maxsize=None)
    def dp(self, s, i, k):
        if k == 1:
            return self.cost(s, i, len(s) - 1)
        res = math.inf
        for j in range(i, len(s)):
            res = min(res, self.cost(s, i, j) + self.dp(s, j + 1, k - 1))
        return res


