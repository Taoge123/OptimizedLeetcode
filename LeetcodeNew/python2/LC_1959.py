"""

1 23456
12 3456
123 456
1234 56
12345 6

"""


import functools

class Solution:
    def minSpaceWastedKResizing(self, nums, k: int) -> int:

        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i, k):
            if i == n:
                return 0
            if k < 0:
                return float('inf')

            res = float('inf')
            maxi = nums[i]
            summ = 0
            for j in range(i, n):
                maxi = max(maxi, nums[j])
                summ += nums[j]
                cpst = maxi * (j - i + 1) - summ
                res = min(res, dfs(j + 1, k - 1) + cpst)
            return res

        return dfs(0, k)




