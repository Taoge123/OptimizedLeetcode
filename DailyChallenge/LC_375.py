import functools

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        nums = [i for i in range(1, n + 1)]

        @functools.lru_cache(None)
        def dfs(nums, i, j):
            if i >= j:
                return 0

            res = float('inf')
            for k in range(i, j + 1):
                res = min(res, max(dfs(nums, i, k - 1), dfs(nums, k + 1, j)) + nums[k])

            return res

        return dfs(tuple(nums), 0, len(nums) - 1)





