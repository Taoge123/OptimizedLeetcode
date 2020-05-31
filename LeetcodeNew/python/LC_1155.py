"""
https://www.youtube.com/watch?v=J9s7402s5FA
"""

from functools import lru_cache


class Solution:
    def __init__(self):
        self.memo = {}

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if (d, f, target) in self.memo:
            return self.memo[d, f, target]

        mod = 10 ** 9 + 7

        if target < d or target > d * f:
            return 0

        if d == 0:
            return 1 if target == 0 else 0
        res = 0
        for num in range(1, f + 1):
            res += self.numRollsToTarget(d - 1, f, target - num)
        self.memo[d, f, target] = res % mod
        return self.memo[d, f, target]


class SolutionLRU:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10 ** 9 + 7
        return self.dp(d, f, target, mod)

    @lru_cache(None)
    def dp(self, d, f, target, mod):
        if d == 0:
            return 1 if target == 0 else 0

        if target > f * d or target < d:
            return 0

        res = 0

        for k in range(1, f + 1):
            res = (res + self.dp(d - 1, f, target - k, mod)) % mod
        return res
