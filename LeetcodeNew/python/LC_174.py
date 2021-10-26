"""
https://leetcode.com/problems/dungeon-game/discuss/1035135/Memoized-solution-in-python-with-recursion-tree-plotted
https://leetcode.com/problems/dungeon-game/discuss/426346/python-dp
https://leetcode.com/problems/dungeon-game/discuss/447899/Python-Straightforward-Memoization
https://leetcode.com/problems/dungeon-game/discuss/426346/python-dp

"""

import functools


class SolutionTD0:
    def calculateMinimumHP(self, dungeon) -> int:
        m, n = len(dungeon), len(dungeon[0])
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                if dungeon[i][j] <= 0:
                    return abs(dungeon[i][j]) + 1
                else:
                    return 1

            elif i == m or j == n:
                return float("inf")

            res = min(dfs(i + 1, j), dfs(i, j + 1)) - dungeon[i][j]
            if res <= 0:
                return 1
            else:
                return res

        return dfs(0, 0)



class SolutionTD1:
    def calculateMinimumHP(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        @functools.lru_cache(None)
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return max(1, -grid[m - 1][n - 1] + 1)

            if i >= m or j >= n:
                return float('inf')

            return max(1, min(dp(i + 1, j), dp(i, j + 1)) - grid[i][j])
        return dp(0, 0)



class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1]= max(1, 1 - dungeon[-1][-1])
        for j in range(n-2, -1, -1):
            dp[-1][j] = max(dp[-1][j+1] - dungeon[-1][j], 1)

        for i in range(m-2, -1, -1):
            dp[i][-1] = max(dp[i+1][-1] - dungeon[i][-1], 1)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        for i in dungeon:
            print(i)
        return dp[0][0]


    def calculateMinimumHP2(self, dungeon):
        if not dungeon:
            return
        r, c = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in range(c-2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1]-dungeon[-1][i])

        for i in range(r-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])

        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])


        return dp[0][0]


dungeon = [[-1,-2,-3],
           [-4,-5,-6],
           [-7,-8,-9]
           ]
#
# dungeon = [[1,2,3],
#            [4,5,6],
#            [7,8,9]
#            ]

a = Solution()
print(a.calculateMinimumHP(dungeon))




