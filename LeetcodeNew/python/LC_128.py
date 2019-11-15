"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


"""


class Solution:
    def longestConsecutive(self, nums):

        cache = set(nums)
        res = 0

        for i in nums:
            if i - 1 not in cache:
                j = i
                while j in cache:
                    j += 1
                res = max(res, j - i)

        return res


