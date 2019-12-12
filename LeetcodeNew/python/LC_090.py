"""
Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.backtrack(nums, 0, [], res)
        return res

    def backtrack(self, nums, index, path, res):

        res.append(path)

        for i in range(index, len(nums)):

            if i > index and nums[i -1] == nums[i]:
                continue
            self.backtrack(nums, i + 1, path + [nums[i]], res)




