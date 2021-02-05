


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
