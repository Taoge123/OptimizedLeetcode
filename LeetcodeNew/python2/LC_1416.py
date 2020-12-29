"""
https://www.youtube.com/watch?v=mdUTRI2FMtU
"""


import functools


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            res = 0
            num = 0
            for i in range(i, len(s)):
                num = num * 10 + int(s[i])
                if num > k:
                    break
                res += dfs( i +1)
                res %= mod
            return res

        return dfs(0)



