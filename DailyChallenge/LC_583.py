

import functools


class SolutionDFS1:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m and j == m:
                return 0

            if i == m or j == n:
                return m - i or n - j

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j + 1)) + 1

        return dfs(0, 0)


class SolutionDFS2:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.dfs(word1, word2, 0, 0, memo)

    def dfs(self, word1, word2, i, j, memo):
        m, n = len(word1), len(word2)
        if (i, j) in memo:
            return memo[(i, j)]

        if i == m and j == n:
            return 0

        if i == m or j == n:
            return m - i or n - j

        if word1[i] == word2[j]:
            res = self.dfs(word1, word2, i + 1, j + 1, memo)
        else:
            res = min(self.dfs(word1, word2, i + 1, j, memo), self.dfs(word1, word2, i, j + 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]

