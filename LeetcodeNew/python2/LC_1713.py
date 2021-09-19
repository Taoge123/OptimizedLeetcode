
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:

        table = {}
        for i, num in enumerate(target):
            table[num] = i

        dp = []
        for num in arr:
            if num in table:
                dp.append(table[num])
        return len(target) - self.lis(dp)


    def lis(self, nums):
        dp = []
        for num in nums:
            i = bisect.bisect_left(dp, num)
            if i >= len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)



