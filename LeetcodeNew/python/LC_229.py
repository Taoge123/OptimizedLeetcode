"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""


import collections

class Solution:
    def majorityElement(self, nums):

        n = len(nums)
        count = collections.Counter(nums)
        res = []

        for k, v in count.items():
            if v > n // 3:
                res.append(k)
        return res




