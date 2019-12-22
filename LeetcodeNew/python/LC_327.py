"""
315. Count of Smaller Numbers After Self
327. Count of Range Sum
493. Reverse Pairs

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
"""

import bisect
import collections


class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:

        presum = [0]
        summ = 0
        res = 0
        for num in nums:
            summ += num
            res += bisect.bisect_right(presum, summ-lower) - bisect.bisect_left(presum, summ-upper)
            bisect.insort_right(presum, summ)
        return res


class Solution2:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:

        presum = [0]
        for n in nums:
            presum.append(presum[-1] + n)

        table = collections.defaultdict(int)

        res = 0
        for num in presum:
            for target in range(lower, upper + 1):
                if num - target in table:
                    res += table[num - target]
            table[num] += 1
        return res


class Solution3:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:

        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return int(lower <= nums[0] <= upper)

        mid = n >> 1
        count = sum([
            self.countRangeSum(array, lower, upper)
            for array in [nums[:mid], nums[mid:]]
        ])

        suffix, prefix = [0] * (mid + 1), [0] * (n - mid + 1)
        for i in range(mid - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        for i in range(mid, n):
            prefix[i - mid + 1] = prefix[i - mid] + nums[i]

        suffix, prefix = suffix[:-1], sorted(prefix[1:])
        count += sum([
            bisect.bisect_right(prefix, upper - s) -
            bisect.bisect_left(prefix, lower - s)
            for s in suffix
        ])

        return count


nums = [-2,5,-1]
lower = -2
upper = 2

a = Solution()
print(a.countRangeSum(nums, lower, upper))





