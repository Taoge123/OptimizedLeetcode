

"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21


Example 2:

Input: 21
Output: -1
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:

        nums = list(str(n))
        length = len(nums)

        i, j = length - 2, length - 1
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i < 0:
            return -1

        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        res = int("".join(nums[:i + 1] + nums[i + 1:][::-1]))

        if res >= 2 ** 31 or res == n:
            return -1

        return res



