
class Solution:
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res = res ^ i

        return res


