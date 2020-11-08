
class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        return self.dfs(s, 0, len(s ) -1, memo)


    def dfs(self, s, i, j, memo):
        if i > j:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        res = self.dfs(s, i+ 1, j, memo) + 1

        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                if k + 1 > j:
                    res = min(res, self.dfs(s, i, k - 1, memo))
                else:
                    res = min(res, self.dfs(s, i, k - 1, memo) + self.dfs(s, k + 1, j, memo))

        memo[(i, j)] = res
        return memo[(i, j)]



