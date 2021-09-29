"""
house robber II with constraint n // 3

https://leetcode-cn.com/problems/pizza-with-3n-slices/solution/py3-by-mao1112-15/
https://leetcode-cn.com/problems/pizza-with-3n-slices/solution/python-dong-tai-gui-hua-by-hao-shou-bu-juan-21/


"""

import functools


class SolutionTony1:
    def maxSizeSlices(self, nums) -> int:
        k = len(nums) // 3
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, j, k):
            # the bottom case will be we only have two slice pizza left.
            # if k==0: good, we alreay have enough pizza, return 0
            # if k==1: good, return the maximum pizza
            # if k==2: impossible.
            if j - i + 1 <= 2:
                if k == 0:
                    return 0
                elif k == 1:
                    return max(nums[i:j + 1])
                else:
                    return float('-inf')

            return max(dfs(i + 2, j, k - 1) + nums[i], dfs(i + 1, j, k))

        return max(dfs(0, n - 2, k), dfs(1, n - 1, k))


class SolutionTony2:
    def maxSizeSlices(self, nums) -> int:
        k = len(nums) // 3
        n = len(nums)
        memo = {}
        return max(self.dfs(nums, 0, n - 2, k, memo), self.dfs(nums, 1, n - 1, k, memo))

    def dfs(self, nums, i, j, k, memo):
        # the bottom case will be we only have two slice pizza left.
        # if k==0: good, we alreay have enough pizza, return 0
        # if k==1: good, return the maximum pizza
        # if k==2: impossible.
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        n = len(nums)
        if j - i + 1 <= 2:
            if k == 0:
                return 0
            elif k == 1:
                return max(nums[i:j + 1])
            else:
                return float('-inf')

        memo[(i, j, k)] = max(self.dfs(nums, i + 2, j, k - 1, memo) + nums[i], self.dfs(nums, i + 1, j, k, memo))
        return memo[(i, j, k)]


class Solution:
    def maxSizeSlices(self, slices):
        @functools.lru_cache(None)
        def dfs(i, j, remain, cycle):
            if remain == 1:
                return max(slices[i:j + 1])
            if j - i + 1 < remain * 2 - 1:
                return -float('inf')
            return max(dfs(i + cycle, j - 2, remain - 1, 0) + slices[j], dfs(i, j - 1, remain, 0))

        return dfs(0, len(slices) - 1, len(slices) // 3, 1)




class SolutionBottomUp:
    def maxSizeSlices(self, slices) -> int:

        def getMax(slices):
            m = len(slices)
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    dp[i][j] = max(dp[i - 1][j], slices[i - 1] + (dp[i - 2][j - 1] if i > 1 else 0))

            return dp[m][n]

        n = len(slices) // 3
        return max(getMax(slices[1:]), getMax(slices[:-1]))




class SolutionComment:
    def maxSizeSlices(self, A):
        @functools.lru_cache(None)
        def dp(i, j, k, cycle=0):
            # i,j = start,end (inclusive)
            # k = remaining
            # cycle (see comment on cycle variable)

            if k == 1:
                # one remaining, calculate immediately
                return max(A[i:j + 1])

            if j - i + 1 < k * 2 - 1:
                # not possible because not enough elements remain
                return -float('inf')

            return max(A[j] +                 # take last element
                       dp(i + cycle, j - 2,   # dp on i to j-2
                          k - 1),             # one less element left to take
                       # (on the cycle variable)
                       # if the last element of the inital array is taken
                       # you cannot take the first element of the inital array
                       # Alternatively, you choose not to take element j
                       dp(i, j - 1,    # dp on i to j-1
                          k))          # same number of elements to take

        return dp(0, len(A) - 1, # dp on 0 to length-1
                  len(A) // 3,   # number of elements to take
                  1)             # see

