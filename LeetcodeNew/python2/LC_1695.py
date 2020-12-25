import collections

class Solution:
    def maximumUniqueSubarray(self, nums) -> int:

        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        res = 0
        left = 0
        last = collections.defaultdict(int)

        for right, num in enumerate(nums):
            # this value occurred before
            if last[num] > 0:
                left = max(left, last[num])

            last[num] = right + 1
            res = max(res, presum[right + 1] - presum[left])

        return res




class Solution2:
    def maximumUniqueSubarray(self, nums) -> int:

        left, right = 0, 0
        res = 0
        summ = 0
        visited = set()
        while right < len(nums):
            if nums[right] in visited:
                summ -= nums[left]
                visited.remove(nums[left])
                left += 1
            else:
                summ += nums[right]
                visited.add(nums[right])
                right += 1

            res = max(res, summ)

        return res
