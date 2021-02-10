"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, nums, target):

        res = []
        self.dfs(nums, target, 0, [], res)
        return res

    def dfs(self, nums, target, pos, path, res):
        if target < 0:
            return

        if target == 0:
            res.append(path)
            return

        for i in range(pos, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


class Solution2:
    def combinationSum(self, nums, target):

        res = []
        self.dfs(nums, target, 0, [], res)
        return res

    def dfs(self, nums, target, pos, path, res):
        if pos == len(nums) and target == 0:
            res.append(path)
            return

        if pos >= len(nums):
            return

        if target < 0:
            return

        # choose
        self.dfs(nums, target - nums[pos], pos, path + [nums[pos]], res)

        # not choose
        self.dfs(nums, target, pos + 1, path, res)

