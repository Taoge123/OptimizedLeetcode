"""
Simple Knapsack problem, dp(i,k) = dp(j,k-1) + cost(s[j+1....i]) for j<i and j+1>=k-1.


"""
"""
https://www.youtube.com/watch?v=kD6ShM6jr3g&t=238s
"""


from functools import lru_cache

class Solution:
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


