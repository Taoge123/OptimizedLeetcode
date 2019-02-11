
"""
Python solution, but it's really easy to understand.
To make it clear for everyone, find following the syntax for get() method of dictionary(hase map)
dict.get(key, default)
The method get() returns a value for the given key. If key is not available then returns default value.
"""

class Solution:

    def findTargetSumWays(self, nums, S):
        count = {0: 1}
        for x in nums:
          count2 = {}
          for tmpSum in count:
            count2[tmpSum + x] = count2.get(tmpSum + x, 0) + count[tmpSum]
            count2[tmpSum - x] = count2.get(tmpSum - x, 0) + count[tmpSum]
          count = count2
        return count.get(S, 0)

"""   
At first I just remember the current index and current target, and for each index, 
either subtract the nums[i] from S or add it to S. But this got TLE, 
them I came up with this solution. Just store the intermediate result with (index, s) 
and this got accepted."""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        def findTarget(i, s):
            if (i, s) not in cache:
                r = 0
                if i == len(nums):
                    if s == 0:
                        r = 1
                else:
                    r = findTarget(i + 1, s - nums[i]) + findTarget(i + 1, s + nums[i])
                cache[(i, s)] = r
            return cache[(i, s)]

        cache = {}
        return findTarget(0, S)


