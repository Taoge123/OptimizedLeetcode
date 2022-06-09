"""
https://leetcode.com/problems/subarray-product-less-than-k/discuss/560093/Python3-two-pointer-O(N)-O(1)-with-breakdown

"""


class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k == 0:
            return 0

        res = 0
        product = 1

        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            res += right - left + 1

        return res



