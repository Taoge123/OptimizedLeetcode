"""
Sliding window
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/discuss/581060/Python-prefix-sum-with-diagram-explanation

So the problem is essentially 2 separate cases.

But it's important to keep in mind that the L+M maximum could be reached before L & M separate from each other
So you cannot divide each case into simply 2 steps:

find the global maximum of the window on the left
find the maximum of the second window in the region to the right of the first window
case 1: L-window comes before M-windows
Once L-window reaches it's global maximum, it will stop sliding but M window can keep going on

case 2: M-window comes before L-windows
Once M-window reaches it's global maximum, it will stop sliding but L window can keep going on
"""

import functools


class SolutionYingjunTonyMemo:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:

        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i, one, two):
            if i >= n:
                return 0
            if one == 0 and two == 0:
                return 0

            no_pick = dfs(i + 1, one, two)
            if one == 0:
                pick = dfs(i + two, 0, 0) + sum(nums[i:i + two])
                return max(no_pick, pick)
            elif two == 0:
                pick = dfs(i + one, 0, 0) + sum(nums[i:i + one])
                return max(no_pick, pick)
            else:
                pick_x = dfs(i + one, 0, two) + sum(nums[i:i + one])
                pick_y = dfs(i + two, one, 0) + sum(nums[i:i + two])
                return max(no_pick, pick_x, pick_y)

        return dfs(0, firstLen, secondLen)



class SolutionOptimizedWithPresum:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i, x, y):
            if i >= n:
                return 0
            if x == 0 and y == 0:
                return 0
            not_pick = dfs(i + 1, x, y)
            # if firstLen is used out, then we will either not pick or pick the current number for secondLen
            if x == 0:
                if i + y >= n:
                    pick = dfs(i + y, 0, 0) + presum[-1] - presum[i]
                else:
                    pick = dfs(i + y, 0, 0) + presum[i + y] - presum[i]
                return max(not_pick, pick)
            elif y == 0:
                if i + x >= n:
                    pick = dfs(i + x, 0, 0) + presum[-1] - presum[i]
                else:
                    pick = dfs(i + x, 0, 0) + presum[i + x] - presum[i]
                return max(not_pick, pick)
            else:
                if i + x >= n:
                    pick_x = dfs(i + x, 0, y) + presum[-1] - presum[i]
                else:
                    pick_x = dfs(i + x, 0, y) + presum[i + x] - presum[i]
                if i + y >= n:
                    pick_y = dfs(i + y, x, 0) + presum[-1] - presum[i]
                else:
                    pick_y = dfs(i + y, x, 0) + presum[i + y] - presum[i]
                return max(not_pick, pick_x, pick_y)

        return dfs(0, firstLen, secondLen)


class SolutionRika:
    def maxSumTwoNoOverlap(self, nums, f: int, s: int) -> int:
        # subarry --> presum
        # get max sum of two subarray

        n = len(nums)
        if n < f + s:
            return 0

        preSum = [nums[0]]
        for i in range(1, len(nums)):
            preSum.append(preSum[-1] + nums[i])

        summ = preSum[f + s - 1]
        firstSum = preSum[f - 1]
        secondSum = preSum[s - 1]

        for i in range(f + s, n):
            curSum_s = preSum[i] - preSum[i - s]
            curSum_f = preSum[i] - preSum[i - f]

            firstSum = max(firstSum, preSum[i - s] - preSum[i - s - f])  # max_firstLen_summ
            secondSum = max(secondSum, preSum[i - f] - preSum[i - s - f])

            # max_firstLen_Summ + current_secondLen_summ vs max_secondLen_Summ + current_firstLen_summ
            summ = max(summ, firstSum + curSum_s, secondSum + curSum_f)

        return summ


class Solution:
    def maxSumTwoNoOverlap(self, nums, one: int, two: int) -> int:
        if len(nums) < one + two:
            return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res, maxL, maxM = nums[one + two - 1], nums[one - 1], nums[two - 1]
        for i in range(one + two, len(nums)):
            maxL = max(maxL, nums[i - two] - nums[i - two - one])
            maxM = max(maxM, nums[i - one] - nums[i - one - two])
            res = max(res, maxL + nums[i] - nums[i - two], maxM + nums[i] - nums[i - one])
        return res

