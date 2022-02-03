
class Solution:
    def findFarmland(self, land):
        res = []
        m, n = len(land), len(land[0])

        def dfs(i, j):
            if i< 0 or i >= m or j < 0 or j >= n or land[i][j] == 0:
                return [0, 0]

            land[i][j] = 0
            row, col = i, j
            for dx, dy in [(1, 0), (0, 1)]:
                x = i + dx
                y = j + dy

                a, b = dfs(x, y)
                row = max(row, a)
                col = max(col, b)
            return [row, col]

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    x, y = dfs(i, j)
                    res.append([i, j, x, y])
        return res






