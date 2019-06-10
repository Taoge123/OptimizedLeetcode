
"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39634/Python-solution-with-detailed-explanation


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e.,
you must sell the stock before you buy again).

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

"""
class Solution1:
    def maxProfit(self, prices):
        if not prices:
            return 0

        # forward traversal, profits record the max profit
        # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)

        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction
        total_max = 0
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])

        return total_max


class Solution2:
    def maxProfit(self, prices):
        max_total_profit = 0
        first_profits = [0] * len(prices)
        min_price = float('inf')

        # Forward phase
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_total_profit = max(max_total_profit, profit)
            first_profits[i] = max_total_profit

        max_price = float('-inf')

        # Backward phase
        for j in range(len(prices) - 1, 0, -1):
            max_price = max(max_price, prices[j])
            profit = max_price - prices[j]
            max_total_profit = max(max_total_profit, first_profits[j - 1] + profit)

        return max_total_profit


class Solution3:
    def maxProfit(self, p):
        if not p: return 0
        sell, buyd, n, minp, maxp = [0], [0], len(p), p[0], p[-1]
        for i in range(1, n):
            minp, maxp = min(minp, p[i]), max(maxp, p[n-i-1])
            sell.append(max(sell[i-1], p[i] - minp))
            buyd.append(max(buyd[i-1], maxp - p[n-i-1]))
        return max(sell[i] + buyd[n-i-1] for i in range(n))



"""
Linear Solution

Consider day i. Say we know maximum profit possible from day 0 to day i. Say we also know the maximum profit from day i+1 to day N-1. Let us call day[i] = forward[i] + backward[i+1]. Backward[i+1] will give us the maximum profit from day i+1 to N-1.
Clearly then, the solution will be max(day[i]).
Now forward[i] is Best Stock 1 problem.
Backward[j[ can also be modelled as the forward[i] problem from j = i+1 to N-1. However this will make it an O(N^2) operation. Can we do it in O(N)?
How about we start from last index and move to 0? Backward[i] is now the reverse problem - start from end, update the highest value as sell value as you move left, and keep updating maximum profit.
Now we will find the cumulative max of both array in respective direction.
Array: [1,2,4,2,5,7,2,4,9,0]
forward: [0, 1, 3, 3, 4, 6, 6, 6, 8, 8]
reverse: [8, 7, 7, 7, 7, 7, 7, 5, 0, 0]
"""


class Solution11:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        N = len(prices)
        forward, backward = [0] * N, [0] * N

        max_so_far, buy = 0, prices[0]
        for i in range(N):
            forward[i] = max(max_so_far, prices[i] - buy)
            max_so_far = max(max_so_far, forward[i])
            buy = min(buy, prices[i])

        max_so_far, sell = 0, prices[-1]
        for i in range(N - 1, -1, -1):
            backward[i] = max(max_so_far, sell - prices[i])
            max_so_far = max(max_so_far, backward[i])
            sell = max(sell, prices[i])

        max_profit = 0
        for i in range(N):
            max_profit_day_i = forward[i] + backward[i + 1] if i < N - 1 else forward[i]
            max_profit = max(max_profit, max_profit_day_i)

        return max_profit


"""
Recursive DP Memoization Solution

f[k, i] represents the max profit up until prices[i] (Note: NOT ending with prices[i]) using at most k transactions.
f[k, i] = max(f[k, i-1], price[i]-price[j] + f[k-1, j-1]) (j in the range of 0 to i-1)
f[k, i] = max(f[k, i-1], price[i] + max( f[k-1, j-1]--price[j])) (j in the range of 0 to i-1)
f[0,i] = 0 (0 times transaction makes 0 profit)
f[k,0] = 0 (if there is only one price data point you can't make any money no matter how many times you can trade)
"""
class Solution2:
    def maxProfit(self, prices):

        if not prices:
            return 0
        N, K = len(prices), 2
        max_profit = -1
        dp = [[0]*N for _ in range(K+1)]
        for k in range(1, K+1):
            tmpMax = dp[k-1][0] - prices[0]
            for i in range(1, N):
                dp[k][i] = max(dp[k][i-1], prices[i] + tmpMax)
                tmpMax = max(tmpMax, dp[k-1][i] - prices[i])
                max_profit = max(max_profit, dp[k][i])
        return dp[K][N-1]



