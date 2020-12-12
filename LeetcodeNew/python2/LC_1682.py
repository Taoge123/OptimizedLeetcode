import functools


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @functools.lru_cache(None)
        def dfs(i, j, prev):
            if i >= j:
                return 0
            if s[i] == s[j] and s[i] != prev:
                return dfs(i + 1, j - 1, s[i]) + 2

            return max(dfs(i + 1, j, prev), dfs(i, j - 1, prev))

        res = dfs(0, len(s) - 1, '#')
        dfs.cache_clear()
        return res





