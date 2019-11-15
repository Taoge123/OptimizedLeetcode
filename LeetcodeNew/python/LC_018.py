import collections

class Solution(object):
    def fourSum(self, nums, target):

        dic = collections.defaultdict(set)
        n = len(nums)
        nums.sort()

        if n < 4:
            return []

        res = set()

        for i in range(n - 1):
            for j in range(i + 1, n):
                sum = nums[i] + nums[j]

                for sub in dic[target - sum]:
                    res.add(tuple(list(sub) + [nums[j], nums[i]]))

            for j in range(i):
                dic[nums[i] + nums[j]].add((nums[j], nums[i]))

        return list(res)

