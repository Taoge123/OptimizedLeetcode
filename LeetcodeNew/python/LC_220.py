"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

"""


import collections

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        if k < 1 or t < 0:
            return False

        table = collections.OrderedDict()
        for num in nums:
            key = num if not t else num // t
            for lastNum in (table.get(key - 1), table.get(key), table.get(key + 1)):
                if lastNum is not None and abs(num - lastNum) <= t:
                    return True
            if len(table) == k:
                table.popitem(False)

            table[key] = num

        return False






