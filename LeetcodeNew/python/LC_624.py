
class Solution:
    def maxDistance(self, arrays):
        res = 0
        mini = 10000
        maxi = -10000
        for nums in arrays:
            res = max(res, max(nums[-1] - mini, maxi - nums[0]))
            mini = min(mini, nums[0])
            maxi = max(maxi, nums[-1])
        return res


