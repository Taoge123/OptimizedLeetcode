
import functools

"""
dp[i][j]: the maximum score we can get from interval [i:j]

for k in range(i, j):
    [i:k] [k+1:j]
    if (leftSum > rightSum)
        dp[i][j] = rightSum + dp[k+1][j]
    else:
        dp[i][j] = leftSum + dp[i][k]
    else:
        dp[i][j] = leftSum/rightSum + max(dp[i][k], dp[k+1][j])


"""




class Solution:
    def stoneGameV(self, stones):
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = stones[i - 1] + preSum[i - 1]
        self.memo = {}
        return self.dfs(0, n - 1, preSum)

    def dfs(self, i, j, preSum):
        if i == j:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        res = -float('inf')
        for k in range(i, j):
            left = preSum[k + 1] - preSum[i]
            right = preSum[j + 1] - preSum[k + 1]
            if left > right:
                res = max(res, right + self.dfs(k + 1, j, preSum))
            elif left < right:
                res = max(res, left + self.dfs(i, k, preSum))
            else:
                res = max(res, left + self.dfs(i, k, preSum), right + self.dfs(k + 1, j, preSum))
        self.memo[(i, j)] = res
        return res






class SolutionTLE:
    def stoneGameV(self, stoneValue) -> int:
        n = len(stoneValue)
        dp = [[0 for i in range( n +1)] for j in range( n +1)]
        stoneValue.insert(0, 0)
        preSum = [0] * ( n +1)
        for i in range(1, n+ 1):
            preSum[i] = preSum[i - 1] + stoneValue[i]
        for i in range(n + 1):
            dp[0][0] = 0

        for i in range(1, n):
            dp[i][i + 1] = min(stoneValue[i], stoneValue[i + 1])

        for step in range(1, n + 1):
            for i in range(1, n - step + 2):
                j = i + step - 1
                for k in range(i, j):
                    leftSum = preSum[k] - preSum[i - 1]
                    rightSum = preSum[j] - preSum[k]
                    if leftSum > rightSum:
                        dp[i][j] = max(dp[i][j], rightSum + dp[k + 1][j])
                    elif leftSum < rightSum:
                        dp[i][j] = max(dp[i][j], leftSum + dp[i][k])
                    else:
                        dp[i][j] = max(dp[i][j], leftSum + max(dp[i][k], dp[k + 1][j]))

        return dp[1][n]




class SolutionLee:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i, a in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j: return 0
            res = 0
            for m in range(i, j):
                left = prefix[m + 1] - prefix[i]
                right = prefix[j + 1] - prefix[m + 1]
                if left <= right:
                    res = max(res, dp(i, m) + left)
                if left >= right:
                    res = max(res, dp(m + 1, j) + right)
            return res

        return dp(0, n - 1)
