class Solution:
    def canPlaceFlowers(self, nums, n: int) -> bool:
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0 and (i == 0 or nums[i - 1] == 0) and (i == len(nums) - 1 or nums[i + 1] == 0):
                nums[i] = 1
                count += 1

            if count >= n:
                return True
            i += 1

        return count >= n



