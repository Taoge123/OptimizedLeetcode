"""
https://www.youtube.com/watch?v=mdUTRI2FMtU
"""


import functools


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(i):
            if i >= n:
                return 1
            if s[i] == '0':
                return 0

            res = 0
            num = 0
            for j in range(i, n):
                num = 10 * num + int(s[j])
                # num = int(s[i:j+1])
                if num > k:
                    break
                if 1 <= num <= k:
                    res += dfs(j + 1)
            return res

        res = dfs(0) % mod
        dfs.cache_clear()
        return res





