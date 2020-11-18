import functools

class SolutionDFS1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        return self.dfs(0, 0, 0, s1, s2, s3, memo)

    def dfs(self, i, j, k, s1, s2, s3, memo):
        m, n, o = len(s1), len(s2), len(s3)
        if i == m and j == n and k == o:
            return True

        if (i == m or j == n) and k == o:
            return False

        if (i, j) in memo:
            return memo[(i, j)]

        res = False
        if i < len(s1) and j < len(s2) and s1[i] == s2[j] and s2[j] == s3[k]:
            res = self.dfs(i + 1, j, k + 1, s1, s2, s3, memo) or self.dfs(i, j + 1, k + 1, s1, s2, s3, memo)

        elif i < len(s1) and s1[i] == s3[k]:
            res = self.dfs(i + 1, j, k + 1, s1, s2, s3, memo)

        elif j < len(s2) and s2[j] == s3[k]:
            res = self.dfs(i, j + 1, k + 1, s1, s2, s3, memo)

        memo[(i, j)] = res
        return memo[(i, j)]


class SolutionDFS2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        @functools.lru_cache(None)
        def dfs(i, j, k, s1, s2, s3):
            m, n, o = len(s1), len(s2), len(s3)
            if i == m and j == n and k == o:
                return True

            if (i == m or j == n) and k == o:
                return False

            if i < len(s1) and j < len(s2) and s1[i] == s2[j] and s2[j] == s3[k]:
                return dfs(i + 1, j, k + 1, s1, s2, s3) or dfs(i, j + 1, k + 1, s1, s2, s3)

            elif i < len(s1) and s1[i] == s3[k]:
                return dfs(i + 1, j, k + 1, s1, s2, s3)

            elif j < len(s2) and s2[j] == s3[k]:
                return dfs(i, j + 1, k + 1, s1, s2, s3)

        return dfs(0, 0, 0, s1, s2, s3)

