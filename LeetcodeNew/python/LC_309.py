
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

"""
"""
buy[i]  = max(rest[i-1] - price, buy[i-1]) 
sell[i] = max(buy[i-1] + price, sell[i-1])
rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
"""

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if not n:
            return 0

        buy = [0] * n
        sell = [0] * n
        cool = [0] * n
        buy[0] = -prices[0]

        for i in range(1, n):
            buy[i] = max(buy[i-1], cool[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            cool[i] = max(cool[i-1], sell[i-1])
        return sell[-1]





