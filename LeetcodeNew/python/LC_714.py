
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        buy = float('-inf')
        sell = 0
        for num in prices:

            buy = max(buy, sell - num)
            sell = max(sell, buy + num - fee)

        return sell



