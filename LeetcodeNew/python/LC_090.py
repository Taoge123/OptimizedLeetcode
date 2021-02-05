"""
https://www.youtube.com/watch?v=mJb7LESm3A8


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
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, pos, path, res):
        res.append(path[:])

        for i in range(pos, len(nums)):
            if i > pos and nums[i - 1] == nums[i]:
                continue

            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)
            path.pop()



nums = [1, 2, 2]
a = Solution()
print(a.subsetsWithDup(nums))

