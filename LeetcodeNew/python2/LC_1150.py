
import bisect

class Solution:
    def isMajorityElement(self, nums, target: int) -> bool:
        n = len(nums)
        if nums[n//2] != target:
            return False

        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        return right - left > n // 2





