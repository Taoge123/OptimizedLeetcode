
"""
2 2 2 2 2 2
[2 2] [2 2] [2 2]
[2 2 2] [2 2 2]

3 3 3 3 3 3 3 3
[3 3] [3 3] [3 3] [3 3]
[3 3 3 3] [3 3 3 3]

find gcd
"""
import collections
import math


class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        count = collections.Counter(deck)
        nums = list(count.values())
        if len(nums) == 1:
            if nums[0] % 2 == 0 and nums[0] >= 2:
                return True
        res = nums[0]
        for i in range(1, len(nums)):
            res = math.gcd(res, nums[i])

        return res >= 2






