class Solution:
    def binaryGap(self, n: int) -> int:
        nums = [i for i in range(32) if (n >> i) & 1]
        if len(nums) < 2:
            return 0

        return max(nums[i + 1] - nums[i] for i in range(len(nums) - 1))


