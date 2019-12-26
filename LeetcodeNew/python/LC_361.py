
"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
Explanation: For the given grid,

0 E 0 0
E 0 W E
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
"""


class Solution:
    def maxKilledEnemies(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        top = [[0] * n for i in range(m)]
        bot = [[0] * n for i in range(m)]
        left = [[0] * n for i in range(m)]
        right = [[0] * n for i in range(m)]

        for i in range(1, m):
            for j in range(n):
                if grid[i - 1][j] == 'W':
                    top[i][j] = 0
                else:
                    top[i][j] = top[i - 1][j] + (grid[i - 1][j] == 'E')
        for i in range(m):
            for j in range(1, n):
                if grid[i][j - 1] == 'W':
                    left[i][j] = 0
                else:
                    left[i][j] = left[i][j - 1] + (grid[i][j - 1] == 'E')

        for i in range(m - 1)[::-1]:
            for j in range(n):
                if grid[i + 1][j] == 'W':
                    bot[i][j] = 0
                else:
                    bot[i][j] = bot[i + 1][j] + (grid[i + 1][j] == 'E')

        for i in range(m):
            for j in range(n - 1)[::-1]:
                if grid[i][j + 1] == 'W':
                    right[i][j] = 0
                else:
                    right[i][j] = right[i][j + 1] + (grid[i][j + 1] == 'E')

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, left[i][j] + right[i][j] + top[i][j] + bot[i][j])
        return res


class Solution2:
    def maxKilledEnemies(self, grid):

        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        dp = [[[0, 0] for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "E":
                    dp[i][j] = [dp[i - 1][j][0] + 1,  + dp[i][j - 1][1] + 1]
                elif grid[i][j] == "0":
                    dp[i][j] = [dp[i - 1][j][0], dp[i][j - 1][1]]

        maxKilled = 0
        for i in reversed(range(0, len(grid))):
            for j in reversed(range(0, len(grid[0]))):
                if j != len(grid[0]) - 1:
                    if grid[i][j + 1] != "W":
                        dp[i][j][1] = dp[i][j + 1][1]
                if i != len(grid) - 1:
                    if grid[i + 1][j] != "W":
                        dp[i][j][0] = dp[i + 1][j][0]
                if grid[i][j] == "0":
                    curKilled = dp[i][j][0] + dp[i][j][1]
                    if curKilled > maxKilled:
                        maxKilled = curKilled

        return maxKilled




class Solution3:
    def maxKilledEnemies(self, grid) -> int:

        if not grid or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        res = 0
        rowCount = 0
        colCount = [0] * n

        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    rowCount = 0
                    for k in range(j, n):
                        if grid[i][k] == 'E':
                            rowCount += 1
                        elif grid[i][k] == 'W':
                            break

                if i == 0 or grid[i - 1][j] == 'W':
                    colCount[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'E':
                            colCount[j] += 1
                        elif grid[k][j] == 'W':
                            break

                if grid[i][j] == '0':
                    res = max(res, rowCount + colCount[j])
        return res


grid = [["0","E","0","0"],
        ["E","0","W","E"],
        ["0","E","0","0"]]

a = Solution3()
print(a.maxKilledEnemies(grid))


