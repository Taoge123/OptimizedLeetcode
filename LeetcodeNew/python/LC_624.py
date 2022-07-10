
class SolutionTony:
    def maxDistance(self, arrays):
        mini = float('inf')
        maxi = float('-inf')
        res = 0
        for nums in arrays:
            res = max(res, nums[-1] - mini, maxi - nums[0])
            mini = min(mini, nums[0])
            maxi = max(maxi, nums[-1])
        return res

