"""
https://www.youtube.com/watch?v=ZBOGrSS_xiM


[1,2,5,9]  threshold = 6

1,2,5,9   threshold = 6



/ divisor -> big -> small

1.
left = 1
right = max(nums)

if summ(mid) >= threshold:
    left = mid + 1
else:
    right = mid
return left

2. helper()

3. equal

"""

import math


class SolutionTony:
    def smallestDivisor(self, nums, threshold: int) -> int:

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if self.count(nums, mid) <= threshold:
                right = mid
            else:
                left = mid + 1
        return left

    def count(self, nums, divisor):
        return sum([math.ceil(num / divisor) for num in nums])


class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        left = 1
        right = 10 ** 7

        while left < right:
            mid = (right - left) // 2 + left
            # res = sum(num // mid + 1 if num % mid else num // mid for num in nums)
            res = sum((num + mid - 1) // mid for num in nums)
            if res > threshold:
                left = mid + 1
            else:
                right = mid

        return left









