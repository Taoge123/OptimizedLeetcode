
class Solution:
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

