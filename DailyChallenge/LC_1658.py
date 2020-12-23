

class Solution:
    def minOperations(self, nums, x: int) -> int:
        n = len(nums)
        res = -1
        target = sum(nums) - x
        left, right = 0, 0
        summ = 0
        while left < n and right < n:
            if right < n:
                summ += nums[right]
                right += 1
            while summ > target and left < n:
                summ -= nums[left]
                left += 1

            if summ == target:
                res = max(res, right - left)

        return n - res if res >= 0 else -1

