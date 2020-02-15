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


nums = [1,4,3,5,6,1,4,3,5]
a = Solution()
print(a.permute(nums))



