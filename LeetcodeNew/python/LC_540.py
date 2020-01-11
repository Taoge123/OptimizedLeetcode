

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.



Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
"""


class Solution:
    def singleNonDuplicate(self, nums) -> int:

        start = 0
        end = len(nums) // 2
        while start < end:
            mid = (start + end) // 2
            if nums[2 * mid] != nums[2 * mid + 1]:
                end = mid
            else:
                start = mid + 1

        return nums[2 * start]


class Solution2:
    def singleNonDuplicate(self, nums) -> int:
        res = 0
        for num in nums:
            res ^= num

        return res




