import collections


class Solution:
    def findShortestSubArray(self, nums) -> int:
        if not nums:
            return 0

        table = collections.defaultdict(list)
        for i in range(len(nums)):
            if nums[i] not in table:
                table[nums[i]] = [1, i, i]
            else:
                table[nums[i]][0] += 1
                table[nums[i]][2] = i

        degree = float('-inf')
        res = float('inf')

        for val, i, j in table.values():
            if val > degree:
                degree = val
                res = j - i + 1
            elif val == degree:
                res = min(res, j - i + 1)

        return res




