"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

"""


class SolutionTony:
    def combinationSum3(self, k: int, n: int):
        nums = [i for i in range(1, 10)]
        res = []
        self.dfs(nums, 0, n, k, [], res)
        return res

    def dfs(self, nums, index, target, k, path, res):
        if target < 0:
            return

        if target == 0 and len(path) == k:
            res.append(path)

        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, target - nums[i], k, path + [nums[i]], res)

        return res


class Solution:
    def combinationSum3(self, k, n):
        res = []
        self.dfs(range(1, 10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, pos, path, res):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(pos, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], res)


