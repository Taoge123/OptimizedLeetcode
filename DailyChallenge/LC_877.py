
class Solution:
    def stoneGame(self, piles) -> bool:
        memo = {}
        return self.dfs(piles, 0, len(piles ) -1, memo)

    def dfs(self, nums, i, j, memo):
        if i == j:
            return nums[i]

        if (i, j) in memo:
            return memo[(i, j)]

        left = nums[i] - self.dfs(nums, i+ 1, j, memo)
        # right = nums[j] - self.dfs(nums, i, j-1, memo)
        memo[(i, j)] = left

        return memo[(i, j)]





