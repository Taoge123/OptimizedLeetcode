



class Solution:
    def combinationSum2(self, nums, target):

        res = []
        nums.sort()
        self.dfs(nums, target, 0, [], res)
        return res

    def dfs(self, nums, target, pos, path, res):
        if target < 0:
            return

        if target == 0:
            res.append(path)
            return

        for i in range(pos, len(nums)):
            if i > pos and nums[i - 1] == nums[i]:
                continue
            if nums[i] > target:
                break

            self.dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)

