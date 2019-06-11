
"""
Say you have an array for which the ith element is the price of a given stock on day i.

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
import collections

class Solution1:
    def max_profit(self, prices, K):
        if K == 0 or prices == []:
            return 0

        days = len(prices)
        num_transactions = K + 1  # 0th transaction up to and including kth transaction is considered.

        T = [[0 for _ in range(days)] for _ in range(num_transactions)]

        for transaction in range(1, num_transactions):
            max_diff = - prices[0]
            for day in range(1, days):
                T[transaction][day] = max(T[transaction][day - 1],  # No transaction
                                          prices[day] + max_diff)  # price on that day with max diff
                max_diff = max(max_diff,
                               T[transaction - 1][day] - prices[day])  # update max_diff

        self.print_actual_solution(T, prices)

        return T[-1][-1]


    def max_profit_slow_solution(self, prices, K):
        if K == 0 or prices == []:
            return 0

        days = len(prices)
        num_transactions = K + 1

        T = [[0 for _ in range(len(prices))] for _ in range(num_transactions)]

        for transaction in range(1, num_transactions):
            for day in range(1, days):
                # This maximum value of either
                # a) No Transaction on the day. We pick the value from day - 1
                # b) Max profit made by selling on the day plus the cost of the previous transaction, considered over m days
                T[transaction][day] = max(T[transaction][day - 1],
                                          max([(prices[day] - prices[m] + T[transaction - 1][m]) for m in range(day)]))

        self.print_actual_solution(self, T, prices)
        return T[-1][-1]


    def print_actual_solution(self, T, prices):
        transaction = len(T) - 1
        day = len(T[0]) - 1
        stack = []

        while True:
            if transaction == 0 or day == 0:
                break

            if T[transaction][day] == T[transaction][day - 1]:  # Didn't sell
                day -= 1
            else:
                stack.append(day)          # sold
                max_diff = T[transaction][day] - prices[day]
                for k in range(day - 1, -1, -1):
                    if T[transaction - 1][k] - prices[k] == max_diff:
                        stack.append(k)  # bought
                        transaction -= 1
                        break

        for entry in range(len(stack) - 1, -1, -2):
            print("Buy on day {day} at price {price}".format(day=stack[entry], price=prices[stack[transaction]]))
            print("Sell on day {day} at price {price}".format(day=stack[entry], price=prices[stack[transaction - 1]]))


"""
I think the general idea has been thoroughly explained by other brilliant leetcoders. 
All of the solutions are beautiful and concise. However, most of the them don't look obvious to me, 
so I wrote this and hope it looks more straight forward.
It's O(kn), apparently not optimal. I name the key variables as local profit and global profit to make things much understandable 
(well, at least , to me). Performance is not too bad though.
"""
class Solution2:
    def maxProfit4(self, k, prices):
        n = len(prices)
        if n < 2:
            return 0
        # k is big enougth to cover all ramps.
        if k >= n / 2:
            return sum(i - j
                       for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        globalMax = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            # The max profit with i transations and selling stock on day j.
            localMax = [0] * n
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                localMax[j] = max(
                    # We have made max profit with (i - 1) transations in
                    # (j - 1) days.
                    # For the last transation, we buy stock on day (j - 1)
                    # and sell it on day j.
                    globalMax[i - 1][j - 1] + profit,
                    # We have made max profit with (i - 1) transations in
                    # (j - 1) days.
                    # For the last transation, we buy stock on day j and
                    # sell it on the same day, so we have 0 profit, apparently
                    # we do not have to add it.
                    globalMax[i - 1][j - 1],  # + 0,
                    # We have made profit in (j - 1) days.
                    # We want to cancel the day (j - 1) sale and sell it on
                    # day j.
                    localMax[j - 1] + profit)
                globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
        return globalMax[k][-1]



class Solution3:
    def maxProfit(self, k, prices):
        # The problem is hard
        # Time complexity, O(nk)
        # Space complexity, O(nk)
        length = len(prices)
        if length < 2:
            return 0
        max_profit = 0
        # if k>= n/2, then it can't complete k transactions. The problem becomes buy-and-sell problem 2
        if k >= length / 2:
            for i in xrange(1, length):
                max_profit += max(prices[i] - prices[i - 1], 0)
            return max_profit

        # max_global[i][j] is to store the maximum profit, at day j, and having i transactions already
        # max_local[i][j] is to store the maximum profit at day j, having i transactions already, and having transaction at day j
        max_global = [[0] * length for _ in xrange(k + 1)]
        max_local = [[0] * length for _ in xrange(k + 1)]

        # i indicates the transaction times, j indicates the times
        for j in xrange(1, length):
            cur_profit = prices[j] - prices[j - 1]  # variable introduced by the current day transaction
            for i in xrange(1, k + 1):
                # max_global depends on max_local, so updata local first, and then global.
                max_local[i][j] = max(max_global[i - 1][j - 1] + max(cur_profit, 0), max_local[i][j - 1] + cur_profit)
                # if cur_profit <0, then the current transaction loses money, so max_local[i][j] = max_global[i-1][j-1]
                # else, it can be max_global[i-1][j-1] + cur_profit, by considering the current transaction
                # or it can be max_local[i][j-1] + cur_profit, this is to CANCEL the last day transaction and moves to the current transaction. Note this doesn't change the total number of transactions. Also, max_local[i-1] has already been considered by max_global[i-1] term
                max_global[i][j] = max(max_global[i][j - 1], max_local[i][j])
                # This is more obvious, by looking at whether transaction on day j has influenced max_global or not.
        return max_global[k][-1]  # the last day, the last transaction


class Solution4:
    def maxProfit(self, k, prices):
        if not prices or not k: return 0
        dp, n = collections.defaultdict(int), len(prices)
        for i in range(1, k + 1):
            diff = -prices[0]
            for j in range(1, n):
                dp[i,j] = max(dp[i,j-1], prices[j] + diff)
                diff = max(diff, dp[i-1, j] - prices[j])
        return dp[k, n-1]



"""
---------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/306438/Python-O(n)-solution-with-thinking-process
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/306427/Different-O(n)-Python-solutions-with-thinking-process
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/306235/Different-DP-Python-solutions-with-thinking-process
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/306282/Different-DP-Python-solutions-with-thinking-process
"""

class Solution11:
    def maxProfit1(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit, min_prev = 0, prices[0]
        for p in prices[1:]:
            if p < min_prev:
                min_prev = p
            else:
                max_profit = max(max_profit, p - min_prev)
        return max_profit


"""
Solution 1: For each day, there are 3 possible actions: buy, sell, nothing.
The action nothing can be interpreted at "sell then immediately buy". So positive changes of prices are profitable.

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(prices[i+1] - prices[i], 0)
        return max_profit
Solution 2: DP algorithm with O(n) time and O(1) space

For each day, there are 3 possible actions: buy, sell, nothing. Let us define
buy[i] = maxProfit of prices[:i+1] with the action buy at day i,
sell[i] = maxProfit of prices[:i+1] with the action sell at day i,
nothing[i] = maxProfit of prices[:i+1] with the action nothing at day i.

The base cases are buy[0] = -prices[0], sell[0] = nothing[0] = 0. The recursive relationships are
buy[i] = max(max(sell[i-1], nothing[i-1]) - prices[i], buy[i-1]) # no cool down
sell[i] = max(buy[i-1] + prices[i], sell[i-1])
nothing[i] = max(sell[i-1], buy[i-1], nothing[i-1]).
"""

class Solution22:
    def maxProfit2(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        prev_buy, prev_sell, prev_nothing = -prices[0], 0, 0
        for i in range(1, n):
            buy = max(max(prev_sell, prev_nothing) - prices[i], prev_buy)
            sell = max(prev_buy + prices[i], prev_sell)
            nothing = max(prev_sell, prev_buy, prev_nothing)
            prev_buy, prev_sell, prev_nothing = buy, sell, nothing
        return max(sell, nothing)


"""
Method 1: naive DP algorithm with O(n^3) time and O(n^2) space
Let dp[i][j] = maxProfit of prices[i:j+1], the base cases and recursive relationship are
(i) dp[i][j] = 0 if i >= j
(ii) dp[i][j] = max(dp[i+1][j], prices[k] - prices[i] + dp[k+2][j] for k from i+1 to j)
Because we have two choices at day i: (1) do nothing at day i, (2) buy at day i, sell at day k, coll down at day k+1.

Solution 1: bottom-top approach with a 2D table (Time Limit Exceeded, 209 / 211 test cases passed.)
"""

class Solution33:
    def maxProfit1(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = dp[i + 1][i + d]
                for k in range(i + 1, i + d + 1):
                    tmp = prices[k] - prices[i]
                    tmp += dp[k + 2][i + d] if k + 2 <= i + d else 0
                    dp[i][i + d] = max(dp[i][i + d], tmp)
        return dp[0][n - 1]

    # Solution 2: top-down approach with memoization (Time Limit Exceeded, 210 / 211 test cases passed.)
    def maxProfit2(self, prices):
        def recursive(i, j):
            if i >= j:
                return 0
            if (i, j) in mp:
                return mp[(i, j)]
            max_profit = recursive(i + 1, j)
            for k in range(i + 1, j + 1):
                tmp = prices[k] - prices[i] + recursive(k + 2, j)
                max_profit = max(max_profit, tmp)
            mp[(i, j)] = max_profit
            return mp[(i, j)]

        mp = {}
        return recursive(0, len(prices) - 1)


"""
Method 2: DP algorithm with O(n) time and O(1) space

For each day, there are 3 possible actions: buy, sell, nothing. Let us define
buy[i] = maxProfit of prices[:i+1] with the action buy at day i,
sell[i] = maxProfit of prices[:i+1] with the action sell at day i,
nothing[i] = maxProfit of prices[:i+1] with the action nothing at day i.

The base cases are buy[0] = -prices[0], sell[0] = nothing[0] = 0.
The recursive relationships are
buy[i] = max(nothing[i-1] - prices[i], buy[i-1]) # if buy at day i then the action at day i-1 must be nothing
sell[i] = max(buy[i-1]+prices[i], sell[i-1])
nothing[i] = max(sell[i-1], buy[i-1], nothing[i-1])."""

class Solution333:
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        prev_buy, prev_sell, prev_nothing = -prices[0], 0, 0
        for i in range(1, n):
            buy = max(prev_nothing - prices[i], prev_buy)
            sell = max(prev_buy + prices[i], prev_sell)
            nothing = max(prev_sell, prev_buy, prev_nothing)
            prev_buy, prev_sell, prev_nothing = buy, sell, nothing
        return max(sell, nothing)



"""
Method 1: naive DP algorithm with O(k n^3) time and O(k n^2) space
Let dp[i][j][k] = maxProfit of prices[i:j+1] with at most k transactions, the base cases and recursive relationship are
(i) dp[i][j][k] = 0 if i >= j or k <= 0
(ii) dp[i][j][k] = max(dp[i+1][j][k], prices[l] - prices[i] + dp[l+1][j][k-1] for l from i+1 to j)
Because we have two choices at day i: (1) do nothing at day i, (2) buy at day i, sell at day l.

Solution 1: bottom-top approach with a 3D table (Time Limit Exceeded, 208 / 211 test cases passed.)
"""
class Solution44:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n < 2:
            return 0
        dp = [[[0 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
        for k1 in range(1, k+1):
            for d in range(1, n):
                for i in range(n - d):
                    dp[i][i+d][k1] = dp[i+1][i+d][k1]
                    for l in range(i+1, i+d+1):
                        tmp = prices[l] - prices[i]
                        tmp += dp[l+1][i+d][k1-1] if l+1 < i+d and k1 - 1 > 0 else 0
                        dp[i][i+d][k1] = max(dp[i][i+d][k1], tmp)
        return dp[0][n-1][k]

    # Solution 2: top-down approach with memoization (Time Limit Exceeded, 208/ 211 test cases passed.)

    def maxProfit2(self, k, prices):
        def recursive(i, j, k):
            if i >= j or k <= 0:
                return 0
            if (i, j, k) in mp:
                return mp[(i, j, k)]
            max_profit = recursive(i + 1, j, k)
            for l in range(i + 1, j + 1):
                tmp = prices[l] - prices[i] + recursive(l + 1, j, k - 1)
                max_profit = max(max_profit, tmp)
            mp[(i, j, k)] = max_profit
            return mp[(i, j, k)]

        mp = {}
        return recursive(0, len(prices) - 1, k)

    """
    Method 2: naive DP algorithm with O(k n^2) time and O(k n) space
    Let dp[i][k] = maxProfit of prices[:i+1] with at most k transactions, the base cases and recursive relationship are
    (i) dp[i][k]= 0 if i <= 0 or k <= 0
    (ii) dp[i][k] = max(dp[i-1][k], prices[i] - prices[j] + dp[j-1][k-1] for j from 0 to i-1)
    Because we have two choices at day i: (1) do nothing at day i, (2) maxProfit of prices[:j+1], buy at day j, sell at day i.

    Solution 3: bottom-top approach with a 2D table (Time Limit Exceeded, 208 / 211 test cases passed.)

    """

    def maxProfit3(self, k, prices):
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        for k1 in range(1, k + 1):
            for i in range(1, n):
                dp[i][k1] = dp[i - 1][k1]
                for j in range(i):
                    tmp = prices[i] - prices[j]
                    tmp += dp[j][k1 - 1] if j > 0 and k1 - 1 > 0 else 0
                    dp[i][k1] = max(dp[i][k1], tmp)
        return dp[n - 1][k]

    # Solution 4: top-down approach with memoization (Time Limit Exceeded, 208 / 211 test cases passed.)
    def maxProfit4(self, k, prices):
        def recursive(i, k):
            if i <= 0 or k <= 0:
                return 0
            if (i, k) in mp:
                return mp[(i, k)]
            max_profit = recursive(i - 1, k)
            for j in range(i):
                tmp = prices[i] - prices[j] + recursive(j - 1, k - 1)
                max_profit = max(max_profit, tmp)
            mp[(i, k)] = max_profit
            return mp[(i, k)]

        mp = {}
        return recursive(len(prices) - 1, k)


    """
    Method 3: DP algorithm with O(k n) time and O(k n) space (beat 45%)
    Let dp[i][k] = maxProfit of prices[:i+1] with at most k transactions, the base cases and recursive relationship are
    (i) dp[i][k]= 0 if i <= 0 or k <= 0
    (ii) dp[i][k] = max(dp[i-1][k], prices[i] - prices[j] + dp[j-1][k-1] for j from 0 to i-1)
    We can further use DP to get local_max = - prices[j] + dp[j-1][k-1] for j from 0 to i-1.
    Solution 5: it is an easier understandable version of https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/188630/C%2B%2B-8-lines-4-ms-DP
    
    """

    def maxProfi5(self, k, prices):
        n = len(prices)
        if n < 2:
            return 0
        if k >= n // 2: # problem 122. Best Time to Buy and Sell Stock II
            max_profit = 0
            for i in range(n - 1):
                max_profit += max(prices[i+1] - prices[i], 0)
            return max_profit
        dp = [[0 for _ in range(k+1)] for _ in range(n)]
        for k1 in range(1, k+1):
            local_max = -prices[0]
            for i in range(1, n):
                dp[i][k1] = max(dp[i-1][k1], prices[i] + local_max)
                local_max = max(local_max, dp[i-1][k1-1] - prices[i])
        return dp[n-1][k]


