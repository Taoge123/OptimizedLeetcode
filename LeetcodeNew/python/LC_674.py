
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums:
            return 0

        if len(nums) <= 1:
            return 1

        count = 1
        res = 1
        for i in range(1, len(nums)):
            if i and nums[ i -1] < nums[i]:
                count += 1
                if count > res:
                    res = count
            else:
                count = 1
        return res



class Solution2:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums:
            return 0

        res = 1
        count = 1

        for i in range(1, len(nums)):
            count = count + 1 if nums[i] > nums[i - 1] else 1
            res = max(res, count)

        return res




