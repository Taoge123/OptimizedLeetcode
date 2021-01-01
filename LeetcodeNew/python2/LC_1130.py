
class SolutionDFS:
    def mctFromLeafValues(self, arr) -> int:
        memo = {}
        return self.dfs(arr, 0, len(arr) - 1, memo)

    def dfs(self, arr, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= j:
            return 0

        res = float('inf')
        for k in range(i, j):
            rootVal = max(arr[i:k + 1]) * max(arr[k + 1:j + 1])
            res = min(res, rootVal + self.dfs(arr, i, k, memo) + self.dfs(arr, k + 1, j, memo))

        memo[(i, j)] = res
        return memo[(i, j)]




class Solution:
    def mctFromLeafValues(self, arr) -> int:
        n = len(arr)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for step in range(2, n + 1):
            for i in range(n - step + 1):
                j = i + step - 1
                for k in range(i, j):
                    rootVal = max(arr[i:k+1]) * max(arr[k+1:j+1])
                    dp[i][j] = min(dp[i][j], rootVal + dp[i][k] + dp[k+1][j])
        return dp[0][n - 1]



