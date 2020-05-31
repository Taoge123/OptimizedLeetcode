"""
https://www.youtube.com/watch?v=ZBOGrSS_xiM
"""


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









