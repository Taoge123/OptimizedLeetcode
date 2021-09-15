
"""
dp[i][k] : minimum total distance between each house and its nearest mailbox for house[0:i] covered by k mailboxed

[XXXXXXX] [XXX i]
  k-i ^
      j

dp[i][k] = min {dp[i][k-1] + range[j+1][i] } for j in 1 ...

X.   X.  X   X.  X
minimize sum|xi-p| -> p = the median {xi}

1478.Allocate-Mailboxes
首先回顾一个引理。一条直线上有若干个点p0,p1,...pn，其median位置处的点是pm，那么该点满足最小化sum{abs(pi-p)}, for i=0,1,...,n

在本题中，我们定义dp[i][k]表示前i个房子的范围内设置k个邮局（或者说设置k个邮局覆盖前i个房子），所得到的最小的objective。我们考虑，那么k-1个邮局可以覆盖多少房子？假设是j个房子。于是我们有一种可能，只要j取得合适，前j个房子被前k-1个邮局覆盖是最优的，并且第j+1到第i个房子被第k个邮局覆盖是最优的。于是就有 dp[i][k] = dp[j][k-1] + range[j+1][i]。其中range[j+1][i]表示区间[j+1,i]内的房子被1个邮局覆盖的objective.显然这1个邮局是位于[j+1,i]的中位数位置，并且range[j+1][i]是可以提前计算出来的。

怎么找到这个合适的j呢？我们可以把所有的j的可能都遍历一遍，最小的dp[j][k-1] + range[j+1][i]就对应着最合适的j。也就是说，不合适的j计算出来的dp[j][k-1] + range[j+1][i]都会偏大，从而不会被dp[i][k]采纳。为什么呢？

举个例子，我们查看某个j。dp[j][k-1]给出了一个k-1个邮局覆盖前j个房子的最优解。range[j+1][i]给出了后面几个房子被1个邮局覆盖的最优解。但是统一来看所有的k个邮局，可能第j个房子更适合被第k个邮局覆盖（距离更近）。如果是这样的话，第j个房子的距离被高估了。同时，前j-1个房子的到邮局距离之和也必然被高估，这是因为如果把第j个划归给第k个邮局的话，前k-1个邮局的规划肯定可以更紧密一些。综上所述，对于不合适的j，整个dp[j][k-1] + range[j+1][i]都会偏大。只有遍历到最合适的j，就能得到dp[j][k-1] + range[j+1][i]的最小值，即最小化dp[i][k]。

"""

"""

4 5684653145431
45 684653145431

4 56 84653145431
45 6 84653145431

456 84653145431
4568 4653145431
45684 653145431
456846 53145431

4568465314543 1

1 4 6 7

3 0 2 3


"""


class SolutionTony:
    def minDistance(self, houses, k: int) -> int:

        memo = {}
        houses.sort()
        return self.dfs(houses, 0, k, memo)

    def dfs(self, nums, i, k, memo):
        # @cache
        # def cost(i, j):
        #     avg = nums[(i + j) // 2]
        #     res = 0
        #     for k in range(i, j + 1):
        #         res += abs(nums[k] - avg)
        #     return res

        if (i, k) in memo:
            return memo[(i, k)]

        n = len(nums)
        if i >= n and k == 0:
            return 0
        if i >= n or k == 0:
            return float('inf')

        res = float('inf')
        summ = 0
        size = 0
        for j in range(i, n):
            summ += nums[j]
            size += 1
            avg = summ // size
            # cost = cost(i, j)
            res = min(res, self.dfs(nums, j + 1, k - 1, memo) + self.cost(nums, i, j))

        memo[(i, k)] = res
        return res

    def cost(self, nums, i, j):
        avg = nums[(i + j) // 2]
        res = 0
        for k in range(i, j + 1):
            res += abs(nums[k] - avg)
        return res


class Solution:
    def minDistance(self, houses, K: int) -> int:
        n = len(houses)
        houses.sort()
        houses.insert(0, float('-inf'))
        dp = [[0 for i in range( K +1)] for j in range( n +1)]

        cover = [[0 for i in range( n +1)] for j in range( n +1)]

        for i in range(1, n+ 1):
            for j in range(i, n + 1):
                cover[i][j] = 0
                for k in range(i, j + 1):
                    cover[i][j] += abs(houses[k] - houses[(i + j) // 2])

        for i in range(1, n + 1):
            dp[i][1] = cover[1][i]

        for i in range(1, n + 1):
            for k in range(2, K + 1):
                dp[i][k] = float('inf')
                for j in range(1, i):
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + cover[j + 1][i])

        return dp[n][K]

