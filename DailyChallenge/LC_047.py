
class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.helper(nums, 0, res)
        return res

    def helper(self, nums, index, res):
        if index == len(nums):
            res.append(nums[:])
        visited = {}
        for i in range(index, len(nums)):
            if visited.get(nums[i]):
                continue
            visited[nums[i]] = True
            nums[i], nums[index] = nums[index], nums[i]
            self.helper(nums, index + 1, res)
            nums[i], nums[index] = nums[index], nums[i]


