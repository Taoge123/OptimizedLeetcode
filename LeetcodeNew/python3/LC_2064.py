
import math


class Solution:
    def minimizedMaximum(self, n, quantities):
        left, right = 1, max(quantities)

        while left < right:
            mid = (right - left) // 2 + left
            if self.count(quantities, mid) <= n:
                right = mid
            else:
                left = mid + 1

        return left


    def count(self, nums, limit):
        count = 0
        for num in nums:
            count += math.ceil(num / limit)
        return count



