


class SolutionTony1:
    def minInsertions(self, s: str) -> int:

        @functools.lru_cache(None)
        def dfs(i, j):
            if j - i < 1:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j - 1)) + 1

        return dfs(0, len(s) - 1)



class SolutionTony2:
    def minInsertions(self, s: str) -> int:
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if j - i < 1:
            return 0
        if s[i] == s[j]:
            memo[(i, j)] = self.dfs(s, i + 1, j - 1, memo)
        else:
            memo[(i, j)] = min(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo)) + 1

        return memo[(i, j)]



