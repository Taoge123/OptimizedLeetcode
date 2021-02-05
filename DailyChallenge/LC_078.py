
class Solution:
    def subsets(self, nums):
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, pos, path, res):
        n = len(nums)
        res.append(path)

        for i in range(pos, n):
            self.dfs(nums, i + 1, path + [nums[i]], res)



