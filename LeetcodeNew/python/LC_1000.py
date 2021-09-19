"""

https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/247567/JavaC%2B%2BPython-DP


这道题的最后一步是将已经merge成K堆的石子做最后一步简单的合并。所以，问题的关键就是变成如何最优化地将原本N堆石子合并成K堆石子，换句话说，需要将[0,N-1]分成K个区间。对于分成K个区间的DP题而言，我们显然会考虑如何先把第一个区间确定，那么其余的就是在剩下的元素里分成K-1个区间。这是比较常见的思路。

所以本题的状态设计为dp[i][j][k]，表示我们将从第i个到第j个元素，拆分成k个区间的最小cost是多少。根据上面的想法，我们需要遍历第一个区间可能的范围（即拆分位置m），寻找最优的拆分。也就是

dp[i][j][k] = min(dp[i][m][1]+dp[m+1][j][k-1]) for i<=m<j
注意，上面的式子里k==1时是没有意义的，因为会导致式子右边的第二项的index变成k-1=0.事实上当k==1的时候，我们单独有：

dp[i][j][1] = dp[i][j][K]+sum[i~j]
就是将初始状态时的第i个石头到第j个石头的重量加起来而已。注意，这个式子仅仅在j-i+1==K的时候有效，其他时候的dp[i][j][1]应该都初始设置为INF。

综上，我们设计基层循环架构：

for (int len = 2; len<=N; len++)
  for (int i=0; i<=N-len; i++)
  {
    int j = i+len-1;    // 这两层循环，我们遍历i,j
    for (int k=2; k<=K; k++)  // 这一层循环我们遍历k
    {
      for (int m=i; m<j; m++) // 这一层循环我们遍历拆分点m，使得分成第一个区间和剩下k-1个区间
      {
        dp[i][j][k] = min(dp[i][m][1]+dp[m+1][j][k-1]) ;
      }
    }
    dp[i][j][1] = dp[i][j][K]+sum[i~j];
  }
return dp[0][N-1][1];
初始值的设计是考虑len==1时的dp[i][j][k]，这种情况下显然k只能也是1，所以dp[i][i][1] = 0;

另外，在上面的更新dp[i][j][1]时，要考虑所有加项必须是有意义的，比如dp[i][m][1]和dp[m+1][j][k-1]不能是无意义的INF。
"""

import functools


class Solution:
    def mergeStones(self, stones, K: int) -> int:
        n = len(stones)
        dp = [[[float('inf') for i in range(K + 1)] for j in range(n)] for i in range(n)]
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + stones[i]

        # 始值的设计是考虑len==1时的dp[i][j][k]，这种情况下显然k只能也是1，所以dp[i][i][1] = 0;
        for i in range(n):
            dp[i][i][1] = 0

        # step是1的时候没法分成2份,没意义
        for step in range(2, n + 1):
            for i in range(n - step + 1):
                j = i + step - 1
                for k in range(2, K + 1):
                    if k > step:
                        continue
                    for m in range(i, j):
                        if dp[i][m][1] == float('inf') or dp[m + 1][j][k - 1] == float('inf'):
                            continue
                        dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m + 1][j][k - 1])
                if dp[i][j][k] != float('inf'):
                    dp[i][j][1] = dp[i][j][k] + preSum[j + 1] - preSum[i]

        if dp[0][n - 1][1] == float('inf'):
            return -1
        return dp[0][n - 1][1]


"""
N
N - (K-1)
N - (K-1)*2
N - (K-1)*3
...
K
1


"""


class SolutionTD:
    def mergeStones(self, nums, K):
        # p = functools.reduce(lambda s,x: s+[s[-1]+x],nums,[0])
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        @functools.lru_cache(None)
        def dfs(i, j, m):
            # if (j-i+1-m) % (K-1):
            #     return float('inf')
            if i == j:
                if m == 1:
                    return 0
                else:
                    return float('inf')
            if m == 1:
                return dfs(i, j, K) + presum[j + 1] - presum[i]

            res = float('inf')
            for k in range(i, j):
                res = min(res, dfs(i, k, 1) + dfs(k + 1, j, m - 1))
            return res

        res = dfs(0, len(nums) - 1, 1)
        return res if res != float('inf') else -1



class SolutionTD2:
    def mergeStones(self, nums, K: int) -> int:
        self.K = K
        self.presum = [0]
        for num in nums:
            self.presum.append(self.presum[-1] + num)

        memo = {}
        res = self.dfs(0, len(nums) - 1, 1, memo)
        return res if res != float('inf') else -1

    def dfs(self, i, j, m, memo):
        if (i, j, m) in memo:
            return memo[(i, j, m)]

        if (j - i + 1 - m) % (self.K - 1):
            return float('inf')
        if i == j:
            if m == 1:
                return 0
            else:
                return float('inf')

        if m == 1:
            return self.dfs(i, j, self.K, memo) + self.presum[j + 1] - self.presum[i]

        res = float('inf')
        for k in range(i, j):
            res = min(res, self.dfs(i, k, 1, memo) + self.dfs(k + 1, j, m - 1, memo))
        memo[(i, j, m)] = res
        return res



class SolutionTopDown:
    def mergeStones(self, stones, K: int) -> int:
        n = len(stones)
        inf = float('inf')
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + stones[i]

        @functools.lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return inf
            if i == j:
                return 0 if m == 1 else inf

            if m == 1:
                return dp(i, j, K) + preSum[j + 1] - preSum[i]

            res = float('inf')
            #mid is the step, we go K-1 step each time
            for mid in range(i, j, K - 1):
                res = min(res, dp(i, mid, 1) + dp(mid + 1, j, m - 1))
            return res

        res = dp(0, n - 1, 1)
        return res if res < inf else -1



nums = [3,2,4,1]
K = 2
a = SolutionTD2()
print(a.mergeStones(nums, K))







