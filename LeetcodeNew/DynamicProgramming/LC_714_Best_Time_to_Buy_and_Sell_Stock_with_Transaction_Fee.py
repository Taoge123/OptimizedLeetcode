
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/242075/intuitive-dp-python

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""

"""
Approach #1: Dynamic Programming [Accepted]
Intuition and Algorithm

At the end of the i-th day, we maintain cash, the maximum profit we could have 
if we did not have a share of stock, and hold, the maximum profit we could have if we owned a share of stock.

To transition from the i-th day to the i+1-th day, 
we either sell our stock cash = max(cash, hold + prices[i] - fee) 
or buy a stock hold = max(hold, cash - prices[i]). 
At the end, we want to return cash. 
We can transform cash first without using temporary variables because selling and buying on the same day can't be better than just continuing to hold the stock.
"""

class Solution1:
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash

"""
The solution maintains two states:

s0 = profit having no stock
s1 = profit having 1 stock
The code iterates through the stock prices, and updates s0, s1 respectively. The run time is O(n).

update s0 by selling the stock from s1, so s0 = max(s0, s1+p);
update s1 by buying the stock from s0, so s1 = max(s1, s0-p-fee);

class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int s0 = 0, s1 = INT_MIN; 
        for(int p:prices) {
            int tmp = s0;
            s0 = max(s0, s1+p);
            s1 = max(s1, tmp-p-fee);
        }
        return s0;
    }
};

"""
class Solution2:
    def maxProfit(self, prices, fee):
        hold, sell = -float('inf'), 0
        for p in prices:
            hold = max(hold, sell - p - fee)
            sell = max(sell, hold + p)
        return sell


"""
buy records the price we buy, and res records the result.
The trick is to buy and sell everytime we can gain a profit 
and twists the buy variable to the sell value minus the fee.
"""
class Solution3:
    def maxProfit(self, prices, fee):

        buy = prices[0]
        res = 0
        for p in prices:
            if buy > p: # current price is less than last buy
                buy = p # buy at p
            else:
                tmp = p - buy - fee
                if tmp > 0: # have profit
                    res += tmp
                    buy = p - fee
        return res












