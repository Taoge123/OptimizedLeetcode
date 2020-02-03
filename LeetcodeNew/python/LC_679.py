

class Solution:
    def judgePoint24(self, nums):
        n = len(nums)
        if n == 1 and abs(nums[0] - 24) < 0.001:
            return True
        for i in range(n):
            for j in range(n):
                if i != j:
                    newNums = [nums[k] for k in range(n) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    if self.judgePoint24(newNums + [a + b]):
                        return True
                    if self.judgePoint24(newNums + [a * b]):
                        return True
                    if self.judgePoint24(newNums + [a - b]):
                        return True
                    if nums[j] != 0 and self.judgePoint24(newNums + [a / b]):
                        return True
        return False


nums = [4, 1, 8, 7]
a = Solution()
print(a.judgePoint24(nums))

