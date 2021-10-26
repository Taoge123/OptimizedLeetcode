"""
741.Cherry-Pickup
本题可以解读为，从左上角到右下角，找出两条可行的线路，使得两条线路采集到的ｃｈｅｒｒｙ数量最多．如果两条线路有重复的部分，则只算一次．

如果只有一条线路，那很明显用ＤＰ算法，每一个点的状态仅仅取决于它左边和上边两个点，转移方程为DP[i][j]＝max{DP[i-1][j],DP[i][j-1]}+grid[i][j]．

那么对于两条线路，我们需要考虑两个点的状态，那么可以设置DP[i][j][x][y]表示的就是两条线路目前的两个位置(i,j),(x,y)．
显然它的状态取决于这两个点分别的左边和上边的两个点．即四个之前的状态：
DP[i][j][x][y]＝max{DP[i-1][j][x-1][y],DP[i][j-1][x-1][y],DP[i][j-1][x-1][y],DP[i][j-1][x][y-1]}
此外还要加上当前的grid[i][j]和grid[x][y]．注意此时等考虑这两个点是否重合：

if (i==x && j==y)
  DP[i][j][x][y]+=grid[i][j]
else
  DP[i][j][x][y]+=grid[i][j]+grid[x][y]
事实上，ＤＰ数组不需要设置为４维．因为i+j=x+y，所以通过三重循环，第四维可以通过y=i+j-x得到．
"""


class SolutionTony:
    def cherryPickup(self, grid):
        memo = {}
        return max(0, self.dfs(grid, 0, 0, 0, 0, memo))

    def dfs(self, grid, x1, y1, x2, y2, memo):
        if (x1, y1, x2) in memo:
            return memo[(x1, y1, x2)]

        m, n = len(grid), len(grid[0])
        if (x1 >= m) or (x2 >= m) or (y1 >= n) or (y2 >= n) or \
                grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return float('-inf')

        res = 0
        if grid[x1][y1] == 1:
            res += 1

        if grid[x2][y2] == 1 and x1 != x2:
            res += 1

        if x1 == m - 1 and y1 == n - 1:
            return res

        res += max(
            self.dfs(grid, x1 + 1, y1, x2 + 1, y2, memo),
            self.dfs(grid, x1 + 1, y1, x2, y2 + 1, memo),
            self.dfs(grid, x1, y1 + 1, x2 + 1, y2, memo),
            self.dfs(grid, x1, y1 + 1, x2, y2 + 1, memo),
        )
        memo[(x1, y1, x2)] = res
        return res


class SolutionWisdom:
    def cherryPickup(self, grid):
        n = len(grid)
        dp = [[[float('-inf') for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0][1][0] = 0
        dp[0][1][1] = 0
        dp[1][0][0] = 0
        dp[1][0][1] = 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for x in range(1, n + 1):
                    y = i + j - x
                    if y < 1 or y > n:
                        continue
                    if grid[i - 1][j - 1] == -1 or grid[x - 1][y - 1] == -1:
                        continue
                    dp[i][j][x] = max(dp[i - 1][j][x], dp[i][j - 1][x], dp[i - 1][j][x - 1], dp[i][j - 1][x - 1])
                    if i == x and j == y:
                        dp[i][j][x] += grid[i - 1][j - 1]
                    else:
                        dp[i][j][x] += grid[i - 1][j - 1] + grid[x - 1][y - 1]

        return max(dp[n][n][n], 0)



class Solution:
    def cherryPickup(self, grid) -> int:
        n = len(grid)
        dp = [[[0 for i in range(n + 1)] for j in range(n + 1)] for k in range(n + 1)]

        for i in range(n + 1):
            for j in range(n + 1):
                for x in range(n + 1):
                    dp[i][j][x] = float('-inf')

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for x in range(1, n + 1):
                    y = i + j - x
                    if y < 1 or y > n:
                        continue

                    if grid[i - 1][j - 1] == -1 or grid[x - 1][y - 1] == -1:
                        continue
                    # It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
                    if i == 1 and j == 1 and x == 1:
                        dp[i][j][x] = grid[0][0]
                        continue

                    dp[i][j][x] = max(dp[i][j][x], dp[i - 1][j][x - 1])
                    dp[i][j][x] = max(dp[i][j][x], dp[i][j - 1][x - 1])
                    dp[i][j][x] = max(dp[i][j][x], dp[i - 1][j][x])
                    dp[i][j][x] = max(dp[i][j][x], dp[i][j - 1][x])

                    if i == x and j == y:
                        dp[i][j][x] += grid[i - 1][j - 1]
                    else:
                        dp[i][j][x] += grid[i - 1][j - 1] + grid[x - 1][y - 1]

        return max(0, dp[-1][-1][-1])


