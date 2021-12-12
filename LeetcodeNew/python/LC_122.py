"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
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

"""

import functools


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        res = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res


class SolutionMemoTLE:
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

        return dfs(0, n, False)



"""[7,1,5,3,6,4]

dp=[           ] 


"""

"""
  [7,1,5,3,6,4]
1  0 0 4 4 5 5      for k in range(i): max(dp[i][j-1], price[i] - price[k]) 
2  0 0 4 4 7 7      for k in range(i): max(dp[i][k]+price[j] - price[k] ])
3  0 0 4 4 7 7
4  0
5  0 

"""
