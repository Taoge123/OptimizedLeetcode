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
        def dfs(i, x, y):
            if i >= n:
                return 0
            if x == 0 and y == 0:
                return 0
            not_pick = dfs(i + 1, x, y)
            # if firstLen is used out, then we will either not pick or pick the current number for secondLen
            if x == 0:
                pick = dfs(i + y, 0, 0) + sum(nums[i:i + y])
                return max(not_pick, pick)
            elif y == 0:
                pick = dfs(i + x, 0, 0) + sum(nums[i:i + x])
                return max(not_pick, pick)
            else:
                pick_x = dfs(i + x, 0, y) + sum(nums[i:i + x])
                pick_y = dfs(i + y, x, 0) + sum(nums[i:i + y])

                return max(not_pick, pick_x, pick_y)

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
                if i + y > n - 1:
                    pick = dfs(i + y, 0, 0) + presum[-1] - presum[i]
                else:
                    pick = dfs(i + y, 0, 0) + presum[i + y] - presum[i]
                return max(not_pick, pick)
            elif y == 0:
                if i + x > n - 1:
                    pick = dfs(i + x, 0, 0) + presum[-1] - presum[i]
                else:
                    pick = dfs(i + x, 0, 0) + presum[i + x] - presum[i]
                return max(not_pick, pick)
            else:
                if i + x > n - 1:
                    pick_x = dfs(i + x, 0, y) + presum[-1] - presum[i]
                else:
                    pick_x = dfs(i + x, 0, y) + presum[i + x] - presum[i]
                if i + y > n - 1:
                    pick_y = dfs(i + y, x, 0) + presum[-1] - presum[i]
                else:
                    pick_y = dfs(i + y, x, 0) + presum[i + y] - presum[i]
                return max(not_pick, pick_x, pick_y)

        return dfs(0, firstLen, secondLen)


class Solution:
    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[ i -1]

        res = A[ L + M -1]
        left = A[ L -1]
        right = A[ M -1]

        for i in range( L +M, len(A)):
            left = max(left, A[ i -M] - A[ i - L -M])
            res = max(res, left + A[i] - A[ i -M])

        for i in range( L +M, len(A)):
            right = max(right, A[ i -L] - A[ i - L -M])
            res = max(res, right + A[i] - A[ i -L])

        return res



