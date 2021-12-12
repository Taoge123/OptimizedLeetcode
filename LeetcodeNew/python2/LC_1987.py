import functools


class Solution:
    def numberOfUniqueGoodSubsequences(self, s):
        mod = 10 ** 9 + 7
        n = len(s)

        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return [0, 0]

            n1, n0 = dfs(i + 1)
            if s[i] == '0':
                n0 = (n0 + n1) + 1
            else:
                n1 = (n0 + n1) + 1
            return [n1, n0]

        res1, res0 = dfs(0)
        return (res1 + ('0' in s)) % mod

