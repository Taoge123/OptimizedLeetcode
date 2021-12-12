"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

import functools

class SolutionMemo:
    def maxProfit(self, nums):
        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i, k, hold):
            if k == 0:
                return 0
            if i == n:
                return 0

            res = dfs(i + 1, k, hold)
            if not hold:
                res = max(res, dfs(i + 1, k, True) - nums[i])
            else:
                res = max(res, dfs(i + 1, k - 1, False) + nums[i])

            return res

        return dfs(0, 1, False)


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit, res = 0, 0
        for i in range(1, len(prices)):
            profit = max(profit + prices[i] - prices[i-1], 0)
            res = max(res, profit)
        return res

class Solution2:
    def maxProfit(self, prices):
        if not prices:
            return 0
        mini, maxi = prices[0], 0
        for i in range(1, len(prices)):
            mini = min(mini, prices[i])
            maxi = max(maxi, prices[i] - mini)
        return maxi


