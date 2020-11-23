import functools


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0

            if s[i] == s[j]:
                return dfs( i +1, j- 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j - 1)) + 1

        return dfs(0, len(s) - 1) <= k



class Solution2:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo) <= k

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= j:
            return 0

        if s[i] == s[j]:
            memo[(i, j)] = self.dfs(s, i+ 1, j - 1, memo)
        else:
            memo[(i, j)] = min(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo)) + 1
        return memo[(i, j)]


