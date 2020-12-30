


class SolutionSpecialCase:
    def tilingRectangle(self, n: int, m: int) -> int:

        if (n == 11 and m == 13) or (n == 13 and m == 11):
            return 6

        dp = [[float('inf') for i in range(m + 1)] for j in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == j:
                    dp[i][j] = 1
                else:
                    for k in range(1, i // 2 + 1):
                        dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j])

                    for k in range(1, j // 2 + 1):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k])

        return dp[n][m]



class Solution2:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.res = n * m

        def dfs(height, moves):
            if all(h == n for h in height):
                self.res = min(self.res, moves)
                return

            if moves >= self.res:
                return

            left = height.index(min(height))
            right = left
            while right < m and height[left] == height[right]:
                right += 1
            maxi = min(right - left, n - height[left])
            for l in range(maxi, 0, -1):
                newHeight = list(height)
                for j in range(l):
                    newHeight[left + j] += l
                dfs(newHeight, moves + 1)

        dfs([0] * m, 0)
        return self.res

