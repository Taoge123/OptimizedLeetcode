import functools


class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:

        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(n, k):
            if n == 0 or k == 0 or k > n:
                return 0
            if k == 1 or k == n:
                return 1
            return k * dfs(n - 1, k) + dfs(n - 1, k - 1)

        res = dfs(n, k) % mod
        dfs.cache_clear()
        return res


class Solution2:
    def waysToDistribute(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(n, k):
            if n == 0:
                return 0
            if k == 1:
                return 1
            return dfs(n - 1, k - 1) + k * dfs(n - 1, k)

        res = dfs(n, k) % mod
        dfs.cache_clear()
        return res


