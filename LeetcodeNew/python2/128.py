
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


