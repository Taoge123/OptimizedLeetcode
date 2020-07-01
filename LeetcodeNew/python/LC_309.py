00000000
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

309.Best-Time-to-Buy-and-Sell-Stock-with-Cooldown
此题和该系列的其他题目一样，用几个状态变量来做DP。此题比较特殊的情况是，仅有hold和sold两个状态是不够的。我们考虑hold表示手头有股票时候的收益，
sold表示手头已经卖出了股票的收益，题目可知我们试图更新sold的时候不能用hold+price[i]，所以我们还需要sold_cd表示手头的股票已经出手了一天以上。

我们不难分析出这三个状态的转移方程是：

hold = max(hold, sold_cd-prices[i])
sold = max(sold, hold+prices[i])
sold_cd = sold
注意所有等号右边的状态变量应该是上一轮的，所以会需要在更新前先缓存一下。


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




