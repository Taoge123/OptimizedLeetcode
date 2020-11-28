
class Solution:
    def missingElement(self, nums, k: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            # to avoid endless loop when l+1==r, you can try to debug in your IDE for (l+r)/2 case.
            mid = (left + right + 1) // 2
            # count the number of missing from the begining to mid point
            if nums[mid] - nums[0] - mid < k:
                left = mid
            else:
                right = mid - 1

        return nums[0] + k + left


class Solution2:
    def missingElement(self, nums, k: int) -> int:
        guess = nums[0] + k
        for i in range(1, len(nums)):

            if nums[i] > guess:
                return guess
            else:
                guess += 1

        return guess






