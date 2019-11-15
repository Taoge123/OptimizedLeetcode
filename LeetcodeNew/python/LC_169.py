

class Solution:
    def majorityElement(self, nums):
        count = 0
        res = nums[0]

        for num in nums[1:]:
            if num == res:
                count += 1
            else:
                count -= 1
                if count < 0:
                    res = num
                    count = 0

        return res

