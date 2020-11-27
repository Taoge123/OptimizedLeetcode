
class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        res = [-1] * len(nums)

        for i in list(range(len(nums))) * 2:
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
