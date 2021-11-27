"""
https://leetcode.com/problems/minimum-incompatibility/discuss/962339/Python-or-2-solutions-or-1-Brute-force-or-1-Memoization-(AC)
https://www.youtube.com/watch?v=aqlZOAt6d80
"""


import itertools
import functools


class Solution:
    def minimumIncompatibility(self, nums, k: int) -> int:
        # the length of each partition
        size = len(nums) // k

        @functools.lru_cache(None)
        def dfs(nums):
            if not nums:
                return 0
            res = float('inf')
            # choose a as a partition
            for comb in itertools.combinations(set(nums), size):
                # check for duplicates
                if len(set(comb)) < size:
                    continue
                # numbers left after removing partition a
                remain = list(nums)
                for num in comb:
                    remain.remove(num)
                res = min(res, max(comb) - min(comb) + dfs(tuple(remain)))
            return res

        res = dfs(tuple(nums)) # turn the input into a tuple so the function can be cached
        return res if res != float('inf') else -1




class SolutionBIT:
    def minimumIncompatibility(self, nums, k: int) -> int:
        size = len(nums) // k
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(state):  # return minimal sum of incompatibilities achievable with unselected indices.
            if state == 0:
                return 0
            else:
                res = float('inf')
                remain = [i for i in range(n) if state & (1 << i)]
                index = itertools.combinations(set(remain), size)
                for idx in list(index):
                    group = [nums[-i - 1] for i in idx]
                    if len(set(group)) < size:
                        continue
                    else:
                        newState = state
                        for i in idx:
                            newState ^= (1 << i)
                        res = min(res, max(group) - min(group) + dfs(newState))

                return res

        res = helper(2 ** n - 1)
        if res == float('inf'):
            return -1
        else:
            return res



