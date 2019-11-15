"""

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


class Solution:
    def permute(self, nums):

        res = []
        self.backtrack(nums, 0, [], res)
        return res

    def backtrack(self, nums, index, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i + 1:], i, path + [nums[i]], res)







