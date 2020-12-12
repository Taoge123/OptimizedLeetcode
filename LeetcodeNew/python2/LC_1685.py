
class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)

        postsum = sum(nums)
        presum = 0

        res = []

        for i in range(len(nums)):
            num = nums[i]
            postsum -= num
            diffleft = (num * i) - presum
            diffright = postsum - num * (n - 1 - i)
            res.append(diffleft + diffright)
            presum += num

        return res


