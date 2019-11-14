class Solution:
    def findMissingRanges(self, nums, lower, upper):

        def getRange(lower, upper):
            if lower == upper:
                return "{}".format(lower)
            else:
                return "{}->{}".format(lower, upper)

        ranges = []
        n = len(nums)
        pre = cur = lower - 1

        for i in range(n + 1):
            if i == n:
                cur = upper + 1
            else:
                cur = nums[i]
            if cur - pre >= 2:
                ranges.append(getRange(pre + 1, cur - 1))
            pre = cur
        return ranges


"""
[0, 1, 3, 50, 75], lower = 0 and upper = 99,


"""

