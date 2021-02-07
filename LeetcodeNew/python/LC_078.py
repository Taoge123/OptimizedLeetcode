"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums):
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, pos, path, res):
        if pos == len(nums):
            res.append(path)
            return res

        self.dfs(nums, pos + 1, path + [nums[pos]], res)
        self.dfs(nums, pos + 1, path, res)




class Solution1:
    def subsets(self, nums):
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, pos, path, res):
        n = len(nums)
        res.append(path)

        for i in range(pos, n):
            self.dfs(nums, i + 1, path + [nums[i]], res)



nums = [1, 2, 3]
a = Solution()
print(a.subsets(nums))


