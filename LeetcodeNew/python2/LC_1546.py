
"""
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/discuss/786169/Java-Recursive-greater-Memoization-greater-DP-Approach
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/discuss/1188324/67-%3A%3A-Python-(Explained)

X [X X X] X [X X] X X X

dp[i]: for the first i elements, the maximum of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target

dp[i] = dp[i-1]

sum[j+1:i] = target = presum[i] - presum[j]

dp[i] = max{dp[j+1]} for j st. taget = presum[i] - presum[j]

dp[n-1]

"""

import functools


class SolutionTDTLE:
    def maxNonOverlapping(self, nums, target: int) -> int:
        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0
            res = 0
            summ = 0
            for j in range(i, n):
                summ += nums[j]
                if summ == target:
                    res = max(res, dfs(j + 1) + 1)
                else:
                    res = max(res, dfs(j + 1))

            return res
        return dfs(0)



class Solution1:
    def maxNonOverlapping(self, nums, target: int) -> int:
        # prsum -> idx
        table = {0: -1}
        n = len(nums)
        presum = [nums[0]]
        for i in range(1, n):
            presum.append(presum[-1] + nums[i])
        res = 0
        left = -1
        for i in range(n):
            if presum[i] - target in table:
                right = table[presum[i] - target]
                if right >= left:
                    res += 1
                    left = i

            table[presum[i]] = i
        return res


class Solution11:
    def maxNonOverlapping(self, nums, target: int) -> int:
        # prsum -> idx
        table = {0: -1}
        n = len(nums)
        presum = 0
        res = 0
        left = -1
        for i in range(n):
            presum += nums[i]
            if presum - target in table:
                right = table[presum - target]
                if right >= left:
                    res += 1
                    left = i

            table[presum] = i
        return res


class Solution2:
    def maxNonOverlapping(self, nums, target: int) -> int:
        # prsum -> idx
        table = {0 : 0}
        n = len(nums)
        presum = [0] * ( n +1)
        for i in range(n):
            presum[ i +1] = presum[i] + nums[i]

        res = 0
        for i in range(1, n+ 1):
            if presum[i] - target in table:
                res += 1
                table = {}

            table[presum[i]] = i
        return res







