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


class Solution1:
    def permute(self, nums):
        n = len(nums)
        res = []
        self.backtrack(nums, n, 0, res)
        return res

    def backtrack(self, nums, n, index, res):
        if index == n:
            res.append(nums[:])
        for i in range(index, n):
            # place i-th integer first
            # in the current permutation
            nums[index], nums[i] = nums[i], nums[index]
            # use next integers to complete the permutations
            self.backtrack(nums, n, index + 1, res)
            # backtrack
            nums[index], nums[i] = nums[i], nums[index]




class Solution11:
    def permute(self, nums):

        res = []
        self.dfs(nums, 0, res)
        return res

    def dfs(self, nums, pos, res):
        if pos == len(nums):
            res.append(nums[:])

        for i in range(pos, len(nums)):
            nums[pos], nums[i] = nums[i], nums[pos]
            self.dfs(nums, pos + 1, res)
            nums[pos], nums[i] = nums[i], nums[pos]




class Solution:
    def permute(self, nums):

        res = []
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)



nums = [1,2,3,4]
a = Solution11()
print(a.permute(nums))



