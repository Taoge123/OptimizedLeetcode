
"""
https://www.youtube.com/watch?v=uySUx0FFly0

"""

import functools
import math

class SolutionTony:
    def maxScore(self, nums) -> int:

        n = len(nums)
        full_mask = 1 << n - 1

        @functools.lru_cache(None)
        def dfs(step, mask):
            # print(mask)
            if mask == full_mask:
                return 0

            res = 0
            for i in range(n):
                if mask & (1 << i) == 0:
                    for j in range(i + 1, n):
                        if mask & (1 << j) == 0:
                            res = max(res, step * math.gcd(nums[i], nums[j]) + dfs(step + 1, mask | (1 << i) | (1 << j)))
            return res

        return dfs(1, 0)


class SolutionDFS:
    def maxScore(self, nums) -> int:
        memo = {}
        res = self.dfs(tuple(nums), 1, memo)  # turn the input into a tuple so the function can be cached
        return res

    def dfs(self, nums, i, memo):
        if (nums, i) in memo:
            return memo[(nums, i)]

        if not nums:
            return 0

        res = float('-inf')
        # choose a as a partition
        for comb in itertools.combinations(nums, 2):
            # print(comb, comb[0])
            remain = list(nums)
            for num in comb:
                remain.remove(num)
            res = max(res, i * gcd(comb[0], comb[1]) + self.dfs(tuple(remain), i + 1, memo))

        memo[(nums, i)] = res
        return memo[(nums, i)]

class SolutionError:
    def maxScore(self, nums) -> int:

        n = len(nums)
        full_mask = 1 << n - 1

        def gcd(a, b):
            a, b = min(a, b), max(a, b)
            if a == 1:
                return b
            return gcd(b // a, a)

        @functools.lru_cache(None)
        def dfs(i, mask):
            # print(mask)
            if mask == full_mask:
                return 0

            res = 0
            for i in range(n):
                if mask & (1 << i) == 0:
                    for j in range(i + 1, n):
                        if mask & (1 << j) == 0:
                            res = max(res, i * gcd(nums[i], nums[j]) + dfs(i + 1, mask | (1 << i) | (1 << j)))
            return res

        return dfs(1, 0)







