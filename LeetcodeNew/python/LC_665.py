
class Solution:
    def checkPossibility(self, nums) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count == 2:
                    return False
                # 3 3 2
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]
                # 1 3 2
                else:
                    nums[i] = nums[i + 1]
        return True



