

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

import collections

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        res, summ = 0, 0
        cache = collections.defaultdict(int)

        cache[0] = 1

        for num in nums:
            summ += num
            res += cache[summ - k]
            cache[summ] += 1

        return res




