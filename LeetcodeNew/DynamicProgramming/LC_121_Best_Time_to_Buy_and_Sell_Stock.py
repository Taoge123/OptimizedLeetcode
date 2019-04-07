
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e.,
buy one and sell one share of the stock), design an algorithm to find the maximum profit.

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

"""
The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm. 
Since no body has mentioned this so far, I thought it's a good thing for everybody to know.

All the straight forward solution should work, but if the interviewer twists the question slightly 
by giving the difference array of prices, Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7}, 
you might end up being confused.

Here, the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) of the original array, 
and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.

public int maxProfit(int[] prices) {
    int maxCur = 0, maxSoFar = 0;
    for(int i = 1; i < prices.length; i++) {
        maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
        maxSoFar = Math.max(maxCur, maxSoFar);
    }
    return maxSoFar;
}
"""

class SolutionCaikehe:
    # DP
    def maxProfit1(self, prices):
        if not prices:
            return 0
        loc = glo = 0
        for i in range(1, len(prices)):
            loc = max(loc + prices[i] - prices[i - 1], 0)
            glo = max(glo, loc)
        return glo

    def maxProfit2(self, prices):
        if not prices:
            return 0
        minPri, maxPro = prices[0], 0
        for i in range(1, len(prices)):
            minPri = min(minPri, prices[i])
            maxPro = max(maxPro, prices[i] - minPri)
        return maxPro

    # Reuse maximum subarray method
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = prices[i] - prices[i - 1]
        glo = loc = dp[0]
        for i in range(1, len(dp)):
            loc = max(loc + dp[i], dp[i])
            glo = max(glo, loc)
        return glo



class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit



class Soution2:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        lenPrices = len(prices)
        state = [0] * lenPrices
        for i in range(1, lenPrices):
            state[i] = max(state[i - 1] + prices[i] - prices[i - 1], 0)

        return max(state)



class Solution3:
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        max_profit=0
        low_price=prices[0]
        for i in range(1,n):
            low_price=min(low_price,prices[i])
            max_profit=max(max_profit, prices[i]-low_price)
        return max_profit




