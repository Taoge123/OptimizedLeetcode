
"""

1000000000000000

10



left = max(nums)
right = sum(nums)

if count() > m:
    left = mid + 1
else:
    right = mid
return left

2.
count()


k
m

1536 113 5136 155 361
9.   11.  15.  11. 10
-> 15

m = 5
1536 113513 615 5361 ->

actual -> chunks < k

guess: 15 -> need it to be smaller


if count(mid) < m:
    left = mid + 1
else:
    right = mid
return left


n * log(n)



153 6113 536 -> m = 3



left = 6

153611 3536 m = 2

right = 34

6 + 34 / 2 -> 20

20 ->


1,2,3   4,5 -> 9

"""

"""
410. Split Array Largest Sum
774. Minimize Max Distance to Gas Station
875. Koko Eating Bananas
1011. Capacity To Ship Packages Within D Days
1231. Divide Chocolate
1201. Ugly Number III
"""

import functools


class SolutionTony:
    def splitArray(self, nums, m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.count(nums, mid) > m:
                left = mid + 1
            else:
                right = mid
        return left

    def count(self, nums, target):
        summ = 0
        count = 0
        for num in nums:
            if num + summ >= target:
                count += 1
                summ = 0
            summ += num
        return count + 1


class SolutionMemo1:
    def splitArray(self, nums, m):
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, m):
            if i == n:
                return 0 if m == 0 else float('inf')

            res = float('inf')
            # total = 0
            for j in range(i, n):
                total = presum[j + 1] - presum[i]
                res = min(res, max(total, dfs(j + 1, m - 1)))
            return res

        return dfs(0, m)



class SolutionMemo11:
    def splitArray(self, nums, m):
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        n = len(nums)
        memo = {}
        return self.dfs(presum, 0, m, memo)

    def dfs(self, presum, i, m, memo):
        if (i, m) in memo:
            return memo[(i, m)]
        n = len(presum) - 1
        if i == n:
            return 0 if m == 0 else float('inf')

        res = float('inf')
        # total = 0
        for j in range(i, n):
            total = presum[j + 1] - presum[i]
            res = min(res, max(total, self.dfs(presum, j + 1, m - 1, memo)))
        memo[(i, m)] = res
        return res



class Solution:
    def splitArray(self, nums, m: int) -> int:
        self.m = m
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (right - left) // 2 + left
            if self.valid(nums, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def valid(self, nums, mid):
        count = 0
        summ = 0
        for num in nums:
            summ += num
            if summ > mid:
                summ = num
                count += 1
                if count >= self.m:
                    return False
        return True




"""

XXX X XXXXXXXXXXXXx
i   k   j    
解法1: DP
大多数的数组问题都可以用动态规划解决。

设计dp[i][k]表示元素1~i分成k份的最佳方案，即最大子区段的最小可能值。

如何设计转移方程呢？无非就是考虑dp[i][k]和这些前态的关系：dp[i-？][k], dp[i][k-？]。
可以发现，dp[i][k]和dp[i-1][k-1]有直接关系。遍历所有将前j个元素（j最小就是k-1）分成k-1份的方案，加上最后一份（就是 sum[i]-sum[j]）的影响。

所以转移方程是： dp[i][k]=min{j} ( max(dp[j][k-1],sum[i]-sum[j]) )

注意的细节是，sum[i]的计算可能会溢出。sum[i]-sum[j]可以转化为 dp[i][1]-dp[j][1].
"""


class SolutionDP:
    def splitArray(self, nums, m: int) -> int:
        n = len(nums)
        dp = [[float('inf') for i in range(m + 1)] for j in range(n + 1)]
        summ = [0 for i in range(n + 1)]

        for i in range(n):
            summ[i + 1] = summ[i] + nums[i]

        dp[0][0] = 0
        for i in range(1, n + 1):
            for k in range(1, m + 1):
                for j in range(i):
                    dp[i][k] = min(dp[i][k], max(dp[j][k - 1], summ[i] - summ[j]))

        return dp[n][m]




