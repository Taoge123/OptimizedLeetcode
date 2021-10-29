
"""
dp[i][j] = dp[i-1][j] for j in [:j] + [j+1:]
"""
"""
1289.Minimum-Falling-Path-Sum-II
此题和265.Paint-House-II本质上一模一样：每一行表示给一座房子涂颜色，每一列表示颜色的种类，
arr[i][j]就是给某座房子涂某种油漆的代价，要求相邻的两座房子不能颜色相同。

状态变量很好定义，dp[i][j]就表示从第一行走到(i,j)的最小权重路径。显然走到(i,j)的关键就是前一行在哪个位置停留。
当然，我们希望是在dp[i-1][k] (k=0,1,2,3...,n-1)里面值最小的那个位置。
唯一的顾虑就是如果这个最小值的位置恰好与第j列相同的话，我们只能取的是次小值。

因为我们在更新第i行的dp值时，可以预先将第i-1行的dp值从小到大排个序。其中的最小值Min在大多数的时候，
都是可以在计算dp[i][j]时共享的，即

dp[i][j] = Min + arr[i][j]
只有一处的j会和Min的列相同，那个时候dp[i][j]就该取次小值。
"""

import heapq
import functools

class SolutionTony:
    def minFallingPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m:
                return 0
            res = float('inf')
            for k in range(n):
                if k == j:
                    continue
                res = min(res, grid[i][k] + dfs(i + 1, k))
            return res

        return dfs(0, n)



class Solution:
    def minFallingPathSum(self, arr) -> int:
        m, n = len(arr), len(arr[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for j in range(n):
            dp[0][j] = arr[0][j]

        for i in range(1, m):
            temp = []
            for k in range(n):
                temp.append([dp[i - 1][k], k])
            temp.sort()

            for j in range(n):
                if j != temp[0][1]:
                    dp[i][j] = temp[0][0] + arr[i][j]
                else:
                    dp[i][j] = temp[1][0] + arr[i][j]

        return min(dp[-1])


class SolutionLee:
    def minFallingPathSum(self, arr) -> int:
        m, n = len(arr), len(arr[0])

        for i in range(1, m):
            node = heapq.nsmallest(2, arr[i - 1])
            for j in range(n):
                if arr[i - 1][j] == node[0]:
                    arr[i][j] += node[1]
                else:
                    arr[i][j] += node[0]
        return min(arr[-1])


