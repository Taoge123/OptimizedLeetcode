
class Solution:
    def createTargetArray(self, nums, index):
        res = []
        for i, num in zip(index, nums):
            res.insert(i, num)
        return res





