
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





