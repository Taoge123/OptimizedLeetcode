


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
