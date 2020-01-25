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


class Solution2:
    def majorityElement(self, nums):
        res = []
        a, b, count1, count2 = 0, 0, 0, 0
        n = len(nums)

        for num in nums:
            if num == a:
                count1 += 1
            elif num == b:
                count2 += 1
            elif count1 == 0:
                a = num
                count1 = 1
            elif count2 == 0:
                b = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if num == a:
                count1 += 1
            elif num == b:
                count2 += 1

        if count1 > n / 3:
            res.append(a)
        if count2 > n / 3:
            res.append(b)

        return res





