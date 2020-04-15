"""
315. Count of Smaller Numbers After Self
327. Count of Range Sum
https://leetcode.com/problems/count-of-range-sum/discuss/407655/Python-different-concise-solutions
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
"""
建议去看 leetcode 315, 327, 493 这些题都可以用这个套路叫BIT + rank
这道题对于每个preSum 我们需要数比他小的数量，BIT 其实就是用来记录每个preSum 出现的频率用的
sort是为了rank所有prefixsum的大小，让BIT可以知道哪些preSum应该放在前面的node 哪些放在后面的node.
"""

import bisect
import collections


class BinaryIndexTree:
    def __init__(self, n):
        self.BIT = [0] * (n + 1)

    def _lowbit(self, i):
        return i & -i

    def query(self, i):
        count = 0
        while i > 0:
            count += self.BIT[i]
            i -= i & -i
        return count

    def update(self, i):
        while i < len(self.BIT):
            self.BIT[i] += 1
            i += i & -i


class Solution:
    def countRangeSum(self, nums, lower, upper):
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)

        sortedSum = sorted(preSum)
        res = 0

        self.len = len(preSum)
        tree = BinaryIndexTree(self.len)

        for num in preSum:
            right = bisect.bisect_right(sortedSum, num - lower)
            left = bisect.bisect_left(sortedSum, num - upper)
            res += tree.query(right) - tree.query(left)
            tree.update(bisect.bisect_right(sortedSum, num))
        return res

"""
nums = [5, 2, 6, 1]
preSum = [0, 5, 7, 13, 14]
sorted = [0, 5, 7, 13, 14]
[0, 0, 0, 0, 0, 0] - 0  -2
[0, 1, 1, 0, 1, 0] - 5  3
[0, 1, 2, 0, 2, 0] - 7  5
[0, 1, 2, 1, 3, 0] - 13 11
[0, 1, 2, 1, 4, 0] - 14 12

nums = [-2, 5, -1, 7, -3, 6]
preSum = [0, -2, 3, 2, 9, 6, 12]
sorted = [-2, 0, 2, 3, 6, 9, 12]
[0, 0, 0, 0, 0, 0, 0, 0] -  0 0
[0, 0, 1, 0, 1, 0, 0, 0] -  0 0
[0, 1, 2, 0, 2, 0, 0, 0] -  2 2
[0, 1, 2, 0, 3, 0, 0, 0] -  2 1
[0, 1, 2, 1, 4, 0, 0, 0] -  4 4
[0, 1, 2, 1, 4, 0, 1, 0] -  4 4
[0, 1, 2, 1, 4, 1, 2, 0] -  6 6



"""


class Solution11:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        presum = [0]
        summ = 0
        res = 0
        for num in nums:
            summ += num
            right = bisect.bisect_right(presum, summ - lower)
            left = bisect.bisect_left(presum, summ - upper)
            res += right - left
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
    # prefix-sum + merge-sort | time complexity: O(nlogn)
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        preSum = [0]
        for n in nums:
            preSum.append(preSum[-1] + n)
        return self.mergesort(preSum, 0, len(preSum) - 1, lower, upper)

    # inclusive
    def mergesort(self, preSum, left, right, lower, upper):
        if left == right:
            return 0
        mid = (left + right) // 2
        res = self.mergesort(preSum, left, mid, lower, upper) \
              + self.mergesort(preSum, mid + 1, right, lower, upper)

        i = j = mid + 1
        # O(n)
        for num in preSum[left:mid + 1]:
            while i <= right and preSum[i] - num < lower:
                i += 1
            while j <= right and preSum[j] - num <= upper:
                j += 1
            res += j - i

        preSum[left:right + 1] = sorted(preSum[left:right + 1])
        return res



nums = [-2, 5, -1, 7, -3, 6]
lower = 0
upper = 2

a = Solution()
print(a.countRangeSum(nums, lower, upper))





