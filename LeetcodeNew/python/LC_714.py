
import functools

class SolutionMemo:
    def maxProfit(self, nums, fee: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, has_stock):
            if i >= len(nums):
                return 0

            res = dfs(i + 1, has_stock)

            if not has_stock:
                res = max(res, dfs(i + 1, True) - nums[i] - fee)
            else:
                res = max(res, dfs(i + 1, False) + nums[i])

            return res

        return dfs(0, False)


class SolutionTony:
    def maxProfit(self, prices, fee: int) -> int:

        memo = {}
        return self.dfs(prices, 0, False, fee, memo)

    def dfs(self, nums, i, has_stock, fee, memo):

        if (i, has_stock) in memo:
            return memo[(i, has_stock)]

        if i >= len(nums):
            return 0

        res = self.dfs(nums, i + 1, has_stock, fee, memo)

        if not has_stock:
            res = max(res, self.dfs(nums, i + 1, True, fee, memo) - nums[i] - fee)
        else:
            res = max(res, self.dfs(nums, i + 1, False, fee, memo) + nums[i])

        memo[(i, has_stock)] = res
        return res



class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        buy = float('-inf')
        sell = 0
        for num in prices:

            buy = max(buy, sell - num)
            sell = max(sell, buy + num - fee)

        return sell



