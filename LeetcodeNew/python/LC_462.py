
"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

"""

import math

import math


class Solution:
    def minMoves2(self, nums) -> int:
        nums = sorted(nums)

        #         left = 0
        #         right = len(nums) - 1
        #         res = 0

        #         while left < right:
        #             res += (nums[right] - nums[left])
        #             right -= 1
        #             left += 1

        #         return res

        # Find the mid element and then use all elements to subtract the mid element

        mid = nums[len(nums) // 2]
        return sum(abs(num - mid) for num in nums)





