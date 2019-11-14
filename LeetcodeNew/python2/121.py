
# class Solution:
#     def maxProfit(self, prices):
#         if not prices:
#             return 0
#         profit, res = 0, 0
#         for i in range(1, len(prices)):
#             profit = max(profit + prices[i] - prices[i-1], 0)
#             res = max(res, profit)
#         return res

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        mini, maxi = prices[0], 0
        for i in range(1, len(prices)):
            mini = min(mini, prices[i])
            maxi = max(maxi, prices[i] - mini)
        return maxi


