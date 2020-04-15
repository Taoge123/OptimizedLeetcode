"""
750	Number Of Corner Rectangle
964	Least Operators to Express Number
730 Count Different Palindromic Subsequences python


class Solution:
    def PredictTheWinner(self, nums):
        cache = {}
        return self.helper(nums, 0, len(nums) - 1, cache) >= 0

    def helper(self, nums, i, j, cache):
        if (i, j) not in cache:
            if i == j:
                return nums[i]
            cache[i, j] = max(nums[i] - self.helper(nums, i + 1, j, cache),
                              nums[j] - self.helper(nums, i, j - 1, cache))

        return cache[i, j]
















"""