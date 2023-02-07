
import functools

class Solution:
    def minCapability(self, nums, k: int) -> int:
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, k):
            if k <= 0:
                return 0

            if i >= n:
                return float('inf')

            rob = max(dfs(i + 2, k - 1), nums[i])
            no_rob = dfs(i + 1, k)
            return min(rob, no_rob)

        return dfs(0, k)

