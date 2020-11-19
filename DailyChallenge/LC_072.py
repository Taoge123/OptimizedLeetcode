import functools

class SolutionDFS1:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.dfs(word1, word2, 0, 0, memo)

    def dfs(self, s1, s2, i, j, memo):
        m, n = len(s1), len(s2)
        # if i == m and j == n:
        #     return 0
        if i == m:
            return len(s2) - j

        if j == n:
            return len(s1) - i

        if (i, j) in memo:
            return memo[(i, j)]

        # res = float('inf')
        if s1[i] == s2[j]:
            res = self.dfs(s1, s2, i + 1, j + 1, memo)

        else:
            res = min(self.dfs(s1, s2, i, j + 1, memo),
                      self.dfs(s1, s2, i + 1, j, memo),
                      self.dfs(s1, s2, i + 1, j + 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]





class SolutionDFS2:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m:
                return len(s2) - j

            if j == n:
                return len(s1) - i

            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(dfs(i, j + 1),
                           dfs(i + 1, j),
                           dfs(i + 1, j + 1)) + 1

        return dfs(0, 0)

