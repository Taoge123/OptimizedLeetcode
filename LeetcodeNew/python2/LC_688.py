
class Solution:
    def knightProbability(self, N, K, r, c):
        memo = {}
        self.directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        return self.dfs(r, c, 1, 0, N, K, memo)

    def dfs(self, i, j, p, k, N, K, memo):
        if 0 <= i < N and 0 <= j < N and k < K:
            res = 0
            for dx, dy in self.directions:
                x = i + dx
                y = j + dy
                if (x, y, k) not in memo:
                    memo[(x, y, k)] = self.dfs(x, y, p / 8, k + 1,  N, K, memo)
                res += memo[(x, y, k)]
            return res
        else:
            return (0 <= i < N and 0 <= j < N and p) or 0







