"""

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/1285198/Why-doesnt-this-work-Python-or-Recursion-with-memoization

"""


class SolutionTony:
    def maxProfit(self, prices) -> int:
        memo = {}
        return self.dfs(prices, 0, 2, False, memo)

    def dfs(self, nums, i, k, hold, memo):
        if (i, k, hold) in memo:
            return memo[(i, k, hold)]

        if k == 0:
            return 0
        if i == len(nums):
            return 0

        res = self.dfs(nums, i + 1, k, hold, memo)
        if not hold:
            res = max(res, self.dfs(nums, i + 1, k, True, memo) - nums[i])
        else:
            res = max(res, self.dfs(nums, i + 1, k - 1, False, memo) + nums[i])

        memo[(i, k, hold)] = res
        return res


class Solution:
    def maxProfit(self, prices):
        buy1, buy2 = float('-inf'), float('-inf')
        sell1, sell2 = 0, 0
        for price in prices:
            buy1 = max(buy1, - price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2




class Solution3:
    def maxProfit(self, p):
        if not p: return 0
        sell, buyd, n, minp, maxp = [0], [0], len(p), p[0], p[-1]
        for i in range(1, n):
            minp, maxp = min(minp, p[i]), max(maxp, p[n-i-1])
            sell.append(max(sell[i-1], p[i] - minp))
            buyd.append(max(buyd[i-1], maxp - p[n-i-1]))
        return max(sell[i] + buyd[n-i-1] for i in range(n))



class Solution4:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        # forward traversal, profits record the max profit
        # by the ith day, this is the first transaction
        profits = []
        profit = 0
        mini = prices[0]
        for price in prices:
            mini = min(mini, price)
            profit = max(profit, price - mini)
            profits.append(profit)

        # backward traversal, profit records the max profit
        # after the ith day, this is the second transaction
        res = 0
        profit = 0
        maxi = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            maxi = max(maxi, prices[i])
            profit = max(profit, maxi - prices[i])
            res = max(res, profit + profits[i])

        return res



class Solution5:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        return self.helper(prices, 2)

    def helper(self, prices, k):
        tran = k + 1
        n = len(prices)
        dp = [[0] * n for _ in range(tran)]

        for k in range(1, tran):
            mini = prices[0]
            for i in range(1, n):
                mini = min(mini, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - mini)
        return dp[-1][-1]



prices = [1,2,3,4,5]
a = Solution4()
print(a.maxProfit(prices))


