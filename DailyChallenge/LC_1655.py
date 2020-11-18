
import collections
import functools


class Solution:
    def canDistribute(self, nums, quantity) -> bool:
        count = collections.Counter(nums)
        nums = sorted(count.values())
        n = len(nums)
        m = len(quantity)
        N = (1 << m) - 1
        table = collections.defaultdict(int)
        for state in range(1, 1 << m):
            for i in range(m):
                if (1 << i) & state:
                    table[state] += quantity[i]
            # print(state, table[state], bin(table[state])[2:])

        @functools.lru_cache(None)
        def dfs(pos, state):
            if state == 0:
                return True

            if pos == n:
                return False

            subset = state
            while subset:
                if table[subset] <= nums[pos] and dfs(pos + 1, state ^ subset):
                    return True
                subset = (subset - 1) & state

            return dfs(pos + 1, state)
        return dfs(0, N)


