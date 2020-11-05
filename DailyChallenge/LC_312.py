
class SolutionTD:
    def maxCoins(self, nums) -> int:
        memo = {}
        nums = [1] + nums + [1]
        return self.dfs(nums, 0, len(nums) - 1, memo)

    def dfs(self, nums, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # if i >= j:
        #     return 0

        res = 0
        for k in range(i + 1, j):
            res = max(res, nums[i] * nums[k] * nums[j] + self.dfs(nums, i, k, memo) + self.dfs(nums, k, j, memo))

        memo[(i, j)] = res
        return memo[(i, j)]


