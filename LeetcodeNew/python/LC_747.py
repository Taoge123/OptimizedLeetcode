class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        res = -1

        for i in range(len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
                res = i
            elif nums[i] > second:
                second = nums[i]

        if first >= second * 2:
            return res
        else:
            return -1




class SolutionTony:
    def dominantIndex(self, nums) -> int:
        if len(nums) <= 1:
            return 0
        List = sorted(nums)
        if List[-1] >= List[-2] * 2:
            return nums.index(List[-1])
        else:
            return -1




