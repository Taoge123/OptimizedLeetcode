
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        count = [0] * ( n +1)
        for num in nums:
            count[num] += 1

        for num in range(1, n+ 1):
            if count[num] == 2:
                twice = num
            if count[num] == 0:
                missing = num
        return [twice, missing]




