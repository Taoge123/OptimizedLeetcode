"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution:
    def permuteUnique(self, nums):

        res = []
        nums = sorted(nums)
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], res)


class Solution2:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.helper(nums, 0, res)
        return res

    def helper(self, nums, index, res):
        if index == len(nums):
            res.append(nums[:])
        visited = {}
        for i in range(index, len(nums)):
            if visited.get(nums[i]):
                continue
            visited[nums[i]] = True
            nums[i], nums[index] = nums[index], nums[i]
            self.helper(nums, index + 1, res)
            nums[i], nums[index] = nums[index], nums[i]





