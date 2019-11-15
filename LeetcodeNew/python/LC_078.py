
class Solution:
    def subsets(self, nums):

        res = []
        nums.sort()
        self.backtrack(nums, 0, [], res)
        return res

    def backtrack(self, nums, index, path, res):
        res.append(path)

        for i in range(index, len(nums)):
            self.backtrack(nums, i + 1, path + [nums[i]], res)


