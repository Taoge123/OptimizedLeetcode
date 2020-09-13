"""
解法1：
因为此题的N为偶数，且不会有平局。说明奇数堆的总和，必然与偶数堆的总和不一样。先手玩家可以总是取奇数堆（或者总是取偶数堆），因此可以必胜。

解法2：
当N为奇数时，就没有上述的巧解。对于这种策略型的题目，递归是比较常见的解法。我们设计递归函数int solve(a,b)表示先手玩家来当前面对[a,b]区间时可以得到的最大收益。因为这个游戏的得分是此消彼长的关系，所以先手玩家最终取得胜利的条件就是：

solve(1,n) > total - solve(1,n);
那么这个递归函数怎么往下拆解呢？无非就是遵循游戏规则，有两种决策：

如果我选择了最左边的石头堆（也就是a），那么对手面临也是同一个最优化的问题，只不过范围不同，即solve(a+1,b)，对手需要在[a+1,b]这个区间内最大化自己的收益。因此我方在[a,b]区间最终能够得到的收益就是sum[a:b] - solve(a+1,b).
如果我选择了最右边的石头堆（也就是b），那么对手面临也是同一个最优化的问题，只不过范围不同，即solve(a,b-1)，对手需要在[a,b-1]这个区间内最大化自己的收益。因此我方在[a,b]区间最终能够得到的收益就是sum[a:b] - solve(a,b-1).
综上，我方必定会在这两个决策中选择一个能够在[a,b]区间收益更多的方案。这就实现了solve(a,b)的递归。无论是我方还是对方，递归的拆解思路总是相同的。递归的边界条件就是a==b时，这堆石头直接拿走。

"""


import collections


class Solution:
    def stoneGame(self, piles) -> bool:
        self.memo = {}
        return self.dfs(piles, 0, len(piles) - 1) > 0

    def dfs(self, piles, i, j):
        # base case
        if i == j:
            return piles[i]

        # dfs with memo
        if (i, j) not in self.memo:
            x = piles[i] - self.dfs(piles, i + 1, j)
            y = piles[j] - self.dfs(piles, i, j - 1)
            self.memo[(i, j)] = max(x, y)

        return self.memo[(i, j)]




class Solution2:
    def stoneGame(self, piles) -> bool:
        memo = {}
        return self.dfs(piles, 0, len(piles)-1, memo) >= 0


    def dfs(self, nums, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            return 0

        if i == j:
            return nums[i]

        if not nums:
            return 0

        res = max(nums[i] - self.dfs(nums, i+1, j, memo), nums[j] - self.dfs(nums, i, j-1, memo))
        memo[(i, j)] = res
        return res


"""
X O X O X O X O

solve(1, n):
    1. pick piles[1] -> piles[1] + sum[2:n] - solve(2, n)      -> sum[1:n] - solve(2, n)
    2. pick piles[n] -> piles[n] + sum[1:n-1] - solve(1, n-1)  -> sum[1:n] - solve(1, n-1)

"""


class SolutionWisdom:
    def stoneGame(self, piles) -> bool:
        n = len(piles)
        piles.insert(0, 0)
        self.cache = collections.defaultdict(int)
        preSum = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + piles[i]

        gain = self.solve(1, n, piles, preSum)
        return gain > preSum[n] - gain

    def solve(self, i, j, piles, preSum):

        if self.cache[(i, j)]:
            return self.cache[(i, j)]
        if i == j:
            return piles[i]
        x = preSum[j] - preSum[i - 1] - self.solve(i + 1, j, piles, preSum)
        y = preSum[j] - preSum[i - 1] - self.solve(i, j - 1, piles, preSum)
        self.cache[(i, j)] = max(x, y)

        return self.cache[(i, j)]


class Solution3:
   def stoneGame(self, p):
       n = len(p)
       dp = p[:]
       for step in range(1, n):
           for i in range(n - d):
               j = i + step
               dp[i] = max(p[i] - dp[i + 1], p[j] - dp[i])
       print(dp)
       return dp[0] > 0



p = [5,3,4,5]
a = Solution()
print(a.stoneGame(p))




