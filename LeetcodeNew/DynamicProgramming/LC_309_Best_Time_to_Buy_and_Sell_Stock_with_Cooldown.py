
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

"""
The series of problems are typical dp. 
The key for dp is to find the variables to represent the states and deduce the transition function.

Of course one may come up with a O(1) space solution directly, 
but I think it is better to be generous when you think and be greedy when you implement.

The natural states for this problem is the 3 possible transactions : 
buy, sell, rest. Here rest means no transaction on that day (aka cooldown).

Then the transaction sequences can end with any of these three states.

For each of them we make an array, buy[n], sell[n] and rest[n].

buy[i] means before day i what is the maxProfit for any sequence end with buy.

sell[i] means before day i what is the maxProfit for any sequence end with sell.

rest[i] means before day i what is the maxProfit for any sequence end with rest.

Then we want to deduce the transition functions for buy sell and rest. By definition we have:

buy[i]  = max(rest[i-1]-price, buy[i-1]) 
sell[i] = max(buy[i-1]+price, sell[i-1])
rest[i] = max(sell[i-1], buy[i-1], rest[i-1])

Where price is the price of day i. All of these are very straightforward. They simply represents :

(1) We have to `rest` before we `buy` and 
(2) we have to `buy` before we `sell`
One tricky point is how do you make sure you sell before you buy, 
since from the equations it seems that [buy, rest, buy] is entirely possible.

Well, the answer lies within the fact that buy[i] <= rest[i] which means rest[i] = max(sell[i-1], rest[i-1]). 
That made sure [buy, rest, buy] is never occurred.

A further observation is that and rest[i] <= sell[i] is also true therefore

rest[i] = sell[i-1]
Substitute this in to buy[i] we now have 2 functions instead of 3:

buy[i] = max(sell[i-2]-price, buy[i-1])
sell[i] = max(buy[i-1]+price, sell[i-1])
This is better than 3, but

we can do even better

Since states of day i relies only on i-1 and i-2 we can reduce the O(n) space to O(1). 
And here we are at our final solution:
"""
"""
buy[i]  = max(rest[i-1]-price, buy[i-1]) 
sell[i] = max(buy[i-1]+price, sell[i-1])
rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
"""

class Solution1:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell


class Solution:
    def maxProfit(self, prices):
        buy, sell, rest = float("-inf"), 0, 0
        for p in prices:
            buy  = max(buy, rest - p)
            sell = max(buy + p, sell)
            rest = max(rest, buy, sell)

        return max(buy, sell, rest)


"""
https://blog.csdn.net/fuxuemingzhu/article/details/82656899

The key is 3 states and 5 edges for state transition. 3 states are notHold (stock), 
hold (stock), and notHold_cooldown. The initial values of the latter two are negative infinity 
since they are meaningless, i.e. you won't hold stocks at first and there's no cooldown at first. 
The 5 edges:

hold -----do nothing----->hold

hold -----sell----->notHold_cooldown

notHold -----do nothing -----> notHold

notHold -----buy-----> hold

notHold_cooldown -----do nothing----->notHold
"""

class Solution2:
    def maxProfit(self, prices):
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold             = max(hold, notHold - p)
            notHold          = max(notHold, notHold_cooldown)
            notHold_cooldown = hold + p
        return max(notHold, notHold_cooldown)


"""
Firstly on any given day we have 2 conditions:
 - Having stock
 - Or not
And we also have 2 more conditions:
 - Having cooldown
 - Or not
In total we assume 2 * 2 = 4 possible conditions on any given day:
 - 0 stock(cool), 0 stock(no-cool), 1 stock(cool), 1 stock(no-cool)
However, we can't have 1 stock(cool) condition, both cooldown(selling) and still having stock.
Let's consider DP for 3 conditions.
 - For 0 stock(cool), we should sell previous day stock = > 1 stock(no-cool)
 - For 0 stock(no-cool), we shouldn't sell anything and have no stock = > 0 stock(cool) or 0 stock(no-cool)
 - For 1 stock(no-cool), we can continue with previous day having 1 stock or buying from 0 stock(no-cool) = > 0 stock(no-cool) or 1 stock(no-cool)
Furthermore, we must initialize start conditions prior to DP like setting 1 stock(no-cool) to minus inifinity for not profiting from fake stock and others to zero.
We should return last day DP conditions without any stock holding for the result.
"""

class Solution3:
    def maxProfit(self, prices):
        # dp1, dp2, dp3 = 0 stock(cool), 0 stock(no-cool), 1 stock(no-cool)
        dp1, dp2, dp3 = 0, 0, -float("inf")
        for p in prices:
            dp1 = dp3 + p
            dp2 = max(dp1, dp2)
            dp3 = max(dp2 - p, dp3)
        return max(dp1, dp2)


class Solution4:
    def maxProfit(self, prices):

        n = len(prices)
        if not prices:
            return 0

        buy = [0] * n
        sell = [0] * n
        cool = [0] * n
        buy[0] = -prices[0]

        for i in range(1, n):
            buy[i] = max(buy[i - 1], cool[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            cool[i] = max(cool[i - 1], sell[i - 1])

        return sell[-1]

"""
题目大意：
给定一个数组，第i个元素代表某只股票在第i天的价格。

设计一个算法计算最大收益。你可以完成多次交易（亦即，多次买入、卖出同一只股票），需要满足下列限制：

你不可以在同一时间参与多个交易（亦即，在买入股票之前必须卖出）。
在卖出股票之后，你不可以在第二天马上买入。（亦即，需要一天的冷却（CD）时间）
测试用例见题目描述。

解题思路：
动态规划（Dynamic Programming）

时间复杂度：O(n)

本题与Best Time to Buy and Sell Stock II唯一的区别是在卖出股票后需要间隔至少一天才能再次买入。
"""

"""
解法I：

引入辅助数组sells和buys

sells[i]表示在第i天卖出股票所能获得的最大累积收益
buys[i]表示在第i天买入股票所能获得的最大累积收益

初始化令sells[0] = 0，buys[0] = -prices[0]
第i天交易时获得的累计收益只与第i-1天与第i-2天有关

记第i天与第i-1天的价格差：delta = price[i] - price[i - 1]

状态转移方程为：

sells[i] = max(buys[i - 1] + prices[i], sells[i - 1] + delta) 
buys[i] = max(sells[i - 2] - prices[i], buys[i - 1] - delta)
上述方程的含义为：

第i天卖出的最大累积收益 = max(第i-1天买入~第i天卖出的最大累积收益, 第i-1天卖出后反悔~改为第i天卖出的最大累积收益)
第i天买入的最大累积收益 = max(第i-2天卖出~第i天买入的最大累积收益, 第i-1天买入后反悔~改为第i天买入的最大累积收益)
而实际上：

第i-1天卖出后反悔，改为第i天卖出 等价于 第i-1天持有股票，第i天再卖出
第i-1天买入后反悔，改为第i天买入 等价于 第i-1天没有股票，第i天再买入
所求的最大收益为max(sells)。显然，卖出股票时才可能获得收益。
"""

class Solution11:
    def maxProfit(self, prices):

        size = len(prices)
        if not size:
            return 0
        buys = [None] * size
        sells = [None] * size
        sells[0], buys[0] = 0, -prices[0]
        for x in range(1, size):
            delta = prices[x] - prices[x - 1]
            sells[x] = max(buys[x - 1] + prices[x], sells[x - 1] + delta)
            buys[x] = max(buys[x - 1] - delta, sells[x - 2] - prices[x] if x > 1 else None)
        return max(sells)


"""
解法II：

引入辅助数组sells和buys

sells[i]表示在第i天不持有股票所能获得的最大累计收益
buys[i]表示在第i天持有股票所能获得的最大累计收益

初始化数组：
sells[0] = 0
sells[1] = max(0, prices[1] - prices[0])
buys[0] = -prices[0]
buys[1] = max(-prices[0], -prices[1])
状态转移方程：

sells[i] = max(sells[i - 1], buys[i - 1] + prices[i])
buys[i] = max(buys[i - 1], sells[i - 2] - prices[i])
所求最大收益为sells[-1]
"""

class Solution22:
    def maxProfit(self, prices):

        size = len(prices)
        if size < 2:
            return 0
        buys = [None] * size
        sells = [None] * size
        sells[0], sells[1] = 0, max(0, prices[1] - prices[0])
        buys[0], buys[1] = -prices[0], max(-prices[0], -prices[1])
        for x in range(2, size):
            sells[x] = max(sells[x - 1], buys[x - 1] + prices[x])
            buys[x] = max(buys[x - 1], sells[x - 2] - prices[x])
        return sells[-1]



