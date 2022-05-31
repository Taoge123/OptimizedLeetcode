

"""

X X X X [i X X j] X X X
sum[i:j] -> prefix[j] - prefix[i-1] = S
prefix[i-1] = prefix[j] - S
"""

import collections

class SolutionSlidingWindow:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        return self.findMost(nums, goal) - self.findMost(nums, goal - 1)

    def findMost(self, nums, k):
        if k < 0:
            return 0
        summ = 0
        count = 0
        left, right = 0, 0

        while right < len(nums):
            summ += nums[right]
            while summ > k:
                summ -= nums[left]
                left += 1
            count += right - left + 1
            right += 1

        return count



class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        table = collections.defaultdict(int)
        table[0] = 1
        summ = 0
        res = 0

        for i in range(len(nums)):
            summ += nums[i]
            if (summ - goal) in table:
                res += table[summ - goal]
            table[summ] += 1
        return res


