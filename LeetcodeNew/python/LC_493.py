"""
315. Count of Smaller Numbers After Self
327. Count of Range Sum
493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""


import bisect
class Solution:
    def reversePairs(self, nums) -> int:
        res = 0
        arr = []
        for i in range(len(nums)):
            index = bisect.bisect_right(arr, 2 * nums[i])
            res += (i - index)
            bisect.insort(arr, nums[i])
        return res



