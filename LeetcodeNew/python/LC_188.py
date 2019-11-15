"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

"""


class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if k > n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        res = [[0] * n for i in range(k + 1)]
        for i in range(1, k + 1):
            local = [0] * n
            for j in range(1, n):
                profit = prices[j] - prices[ j -1]
                local[j] = max(res[ i -1][ j -1] + max(profit, 0), local[ j -1] + profit)
                res[i][j] = max(res[i][ j -1], local[j])
        return res[k][-1]





