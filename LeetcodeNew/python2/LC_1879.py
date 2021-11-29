
"""
x x x x x x x x
o o o o o o o o


"""

import functools


class Solution:
    def minimumXORSum(self, nums1, nums2):

        n = len(nums1)
        @functools.lru_cache(None)
        def dfs(i, mask):
            if i >= n:
                return 0

            res = float('inf')
            for j in range(n):
                if mask & (1 << j) == 0:
                    res = min(res, dfs(i + 1, mask | (1 << j)) + (nums1[i] ^ nums2[j]))

            return res

        return dfs(0, 0)


