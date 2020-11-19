import functools


class SolutionTony:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        return self.dfs(s1, s2, 0, 0, memo)

    def dfs(self, s1, s2, i, j, memo):
        m, n = len(s1), len(s2)
        # if i == m and j == n:
        #     return 0

        if i == m or j == n:
            return sum([ord(i) for i in s1[i:]]) or sum([ord(i) for i in s2[j:]])

        if (i, j) in memo:
            return memo[(i, j)]

        # res = float('inf')
        if s1[i] == s2[j]:
            res = self.dfs(s1, s2, i + 1, j + 1, memo)

        else:
            res = min(self.dfs(s1, s2, i + 1, j, memo) + ord(s1[i]), self.dfs(s1, s2, i, j + 1, memo) + ord(s2[j]))
        memo[(i, j)] = res
        return memo[(i, j)]



class Solution2:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m or j == n:
                return sum([ord(i) for i in s1[i:]]) or sum([ord(i) for i in s2[j:]])

            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1)

            else:
                return min(dfs(i + 1, j) + ord(s1[i]), dfs(i, j + 1) + ord(s2[j]))

        return dfs(0, 0)



