class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}
        return self.dfs(text1, text2, 0, 0, memo)

    def dfs(self, s1, s2, i, j, memo):
        m, n = len(s1), len(s2)
        if i == m or j == n:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        if s1[i] == s2[j]:
            memo[(i, j)] = self.dfs(s1, s2, i + 1, j + 1, memo) + 1

        else:
            memo[(i, j)] = max(self.dfs(s1, s2, i, j + 1, memo), self.dfs(s1, s2, i + 1, j, memo))

        return memo[(i, j)]


class SolutionDFS2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m or j == n:
                return 0

            if text1[i] == text2[j]:
                return dfs(i + 1, j + 1) + 1

            else:
                return max(dfs(i, j + 1), dfs(i + 1, j))

        return dfs(0, 0)