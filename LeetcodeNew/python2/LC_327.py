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
        curr = 0
        res = 0
        for num in nums:
            curr += num
            res += bisect.bisect_right(presum, curr-lower) - bisect.bisect_left(presum, curr-upper)
            bisect.insort_right(presum, curr)
        return res


class Solution2:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:

        presum = [0]
        for n in nums:
            presum.append(presum[-1] + n)

        record = collections.defaultdict(int)

        res = 0
        for num in presum:
            for target in range(lower, upper + 1):
                if num - target in record:
                    res += record[num - target]
            record[num] += 1
        return res



nums = [-2,5,-1]
lower = -2
upper = 2

a = Solution()
print(a.countRangeSum(nums, lower, upper))





