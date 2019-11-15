
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.backtrack(nums, 0, [], res)
        return res

    def backtrack(self, nums, index, path, res):

        res.append(path)

        for i in range(index, len(nums)):

            if i > index and nums[ i -1] == nums[i]:
                continue
            self.backtrack(nums, i + 1, path + [nums[i]], res)






