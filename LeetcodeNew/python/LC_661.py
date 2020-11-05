class Solution:
    def imageSmoother(self, M):
        if not M:
            return M
        m, n = len(M), len(M[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        directions = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    total += M[x][y]
                    count += 1
                dp[i][j] = total // count
        return dp


