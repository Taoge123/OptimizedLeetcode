
class Solution:
    def decompressRLElist(self, nums):
        res = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            res.extend([val] * freq)
        return res


