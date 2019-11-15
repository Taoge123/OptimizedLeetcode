
"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [1] * n

        """
        [1,2,3,4]
        [1,1,1,1]
        [1,1,1,1]
        """

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        temp = 1
        for i in range(n - 2, -1, -1):
            temp *= nums[i + 1]
            res[i] *= temp

        return res




