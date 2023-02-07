"""
we want to know how many subarrays end with arr[i] have odd or even sums

dp[i][0] = # end with arr[i] jas even sum
dp[i][1] = # end with arr[i] jas even sum

if arr[i] is even:
    dp[i][0] = dp[i-1][0] + 1, dp[i][1] = dp[i-1][1]
else:
    dp[i][0] = dp[i-1][1], dp[i][1] = dp[i-1][0] + 1

res = sum(dp[i][1])



"""


import collections

class SolutionTony:
    def numOfSubarrays(self, nums) -> int:

        summ = 0
        res = 0
        table = collections.defaultdict(int)
        table[0] = 1
        for i, num in enumerate(nums):
            summ += nums[i]
            # if summ is odd, then add all previous even count
            if summ % 2 == 1:
                res += table[0]
            # if summ is even, then add all previous odd count
            else:
                res += table[1]
            table[summ % 2] += 1
        return res % (10 ** 9 + 7)



class Solution:
    def numOfSubarrays(self, arr) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7

        dp = [[0] * 2 for i in range(n + 1)]
        res = 0

        for i in range(1, n + 1):
            if arr[i - 1] % 2 == 1:
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = dp[i - 1][0] + 1
            else:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1]

            res += dp[i][1]

        return res % mod



class Solution2:
    def numOfSubarrays(self, arr) -> int:
        mod = 10 ** 9 + 7
        odd, even = 0, 0
        res = 0

        for num in arr:
            if num % 2 == 1:
                odd, even = even + 1, odd
            else:
                odd, even = odd, even + 1

            res += odd
        return res % mod



