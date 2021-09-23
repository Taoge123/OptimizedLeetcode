"""
(i, j, pos)


1 46341463 41
  i      j

15631


"""

import functools


class Solution:
    def maximumScore(self, nums, mul) -> int:
        @functools.lru_cache(None)
        def dfs(i, j, pos):
            n, m = len(nums), len(mul)
            if pos >= m:
                return 0

            left = mul[pos] * nums[i] + dfs(i + 1, j, pos + 1)
            right = mul[pos] * nums[j] + dfs(i, j - 1, pos + 1)
            return max(left, right)

        res = dfs(0, len(nums) - 1, 0)
        dfs.cache_clear()
        return res


