
class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        rob, norob = nums[0], 0

        for i in range(1, len(nums)):
            rob, norob = max(rob, norob + nums[i]), rob
        return max(rob, norob)



